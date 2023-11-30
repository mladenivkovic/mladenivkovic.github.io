#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import subprocess
import os

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

    return "GIT_DATE_ERROR"

    if not _check_git_is_available():
        raise FileNotFoundError("Didn't find git.")

    cmd = 'git log -1 --pretty="format:%ci" '+filename

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
    datestr = datestr[0]

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

    cmd = "pandoc "+filename

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


def write_html_sep(filepointer, stage:str):
    """
    Write a separator with a name between the lines for orientation.
    """

    filepointer.write("\n")
    filepointer.write(html_snippets.separator)
    filepointer.write("<!---  " + stage + " --->\n")
    filepointer.write(html_snippets.separator)
    return


