#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import subprocess
import os
import jinja2

import html_snippets


_pandoc_available = False
_git_available = False


def _check_git_is_available():
    """
    Check whether git is available. Returns True is that is the case.
    """

    global _git_available
    if _git_available:
        return _git_available

    # Does it run?
    cmd = "git --version"

    run = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )

    if run.returncode != 0:
        raise FileNotFoundError("Didn't find git.")

    _git_available = True

    return True


def get_file_date(filename):
    """
    check using git when the file specified by filename
    was last modified.

    filename must be full valid path either relative to
    $workdir or absolute.
    """

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Didn't find file {filename}")

    if not _check_git_is_available():
        raise FileNotFoundError("Didn't find git.")

    cmd = 'git log -1 --pretty="format:%ci" ' + filename

    gitdate = subprocess.run(
        cmd,
        shell=True,
        check=True,
        capture_output=True,
    )
    gitstdout = gitdate.stdout
    if isinstance(gitstdout, bytes):
        gitstdout = gitstdout.decode("utf8")

    dateline = gitstdout.strip()
    datestrlist = dateline.split(" ")
    datestr = datestrlist[0]

    return datestr


def _check_pandoc_is_available():
    """
    Check whether pandoc is available. Returns True is that is the case.
    """
    global _pandoc_available
    if _pandoc_available:
        return _pandoc_available

    # Does it run?
    cmd = "pandoc --version"

    run = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )

    if run.returncode != 0:
        raise FileNotFoundError("Didn't find pandoc.")

    _pandoc_available = True

    return True


def get_html_from_markdown(filename):
    """
    Get html from markdown file specified by `filename`.
    """

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Didn't find crucial file {filename}")

    if not _check_pandoc_is_available():
        raise FileNotFoundError(f"Didn't find pandoc OUTSIDE")

    cmd = "pandoc " + filename

    html = subprocess.run(
        cmd,
        shell=True,
        check=True,
        capture_output=True,
    )
    stdout = html.stdout
    #  if isinstance(stdout, bytes):
    stdout = stdout.decode("utf8")

    return stdout


def write_html_sep(filepointer, stage: str):
    """
    Write a separator with a name between the lines for orientation.
    """

    filepointer.write("\n")
    filepointer.write(html_snippets.separator)
    filepointer.write("<!---  " + stage + " --->\n")
    filepointer.write(html_snippets.separator)
    return


def read_template(filename):
    """
    Read in the jinja template specified by `filename`.
    """

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Didn't find file '{filename}'")

    f = open(filename, "r")
    file_contents = f.read()
    f.close()

    template = jinja2.Template(file_contents)

    return template


def extract_anchor_and_name_from_heading(line: str, sourcefile: str):
    """
    Extract an anchor and a heading from a line of html.

    line: a line of html

    sourcefile: the original markdown source file.

    Returns:

    anchor: Str
        anchor to link to of heading

    name: str
        name of heading

    """

    min_heading_level = 2
    max_heading_level = 4

    # all html heading strings
    all_heading_strings = [f"<h{i}" for i in range(7)]
    filtered_heading_strings = [
        f"<h{i}" for i in range(min_heading_level, max_heading_level + 1)
    ]

    # is this a heading line?
    check = False
    for start in all_heading_strings:
        if line.startswith(start):
            check = True
            break

    if not check:
        return None, None, -1

    # is this a heading line with a level we want?
    check = False
    for start in filtered_heading_strings:
        if line.startswith(start):
            check = True
            break

    found_heading_level = int(line[2])

    if not check:
        print(f"WARNING:", f"Creating Table of Contents for file '{sourcefile}':")
        print(
            "WARNING:", "Found a heading line that will be skipped due to your filters."
        )
        print(
            f"WARNING:",
            f"Min level = {min_heading_level},",
            f"max level = {max_heading_level},",
            f"found = {found_heading_level}",
        )
        print(f"WARNING:", f"Line was: '{line}'")
        print(
            "WARNING:",
            "Check `extract_anchor_and_name_from_heading` to modify this behaviour.",
        )
        print("*****")
        return None, None, -1

    pre, post = line.split('id="')

    i = 0
    anchor = None
    while i < len(post):
        if post[i] == '"':
            anchor = post[:i]
            break
        i += 1

    if anchor is None:
        raise ValueError(f"Didn't detect anchor. Line was '{line}'")

    pre, end = post.split('">')
    i = 0
    name = None
    while i < len(end):
        if end[i] == "<":
            name = end[:i]
            break
        i += 1

    if end[i:] not in ["</h1>", "</h2>", "</h3>", "</h4>", "</h5>"]:
        print(
            "WARNING: Unexpected end of line. Expected header closing tag. Got ",
            end[i:],
            end,
        )
        print(f"WARNING: Full line was '{line}'")
        print(f"WARNING: Source file was '{sourcefile}'")

    if name is None:
        raise ValueError(f"Didn't detect name. Line was '{line}'")

    return anchor, name, found_heading_level
