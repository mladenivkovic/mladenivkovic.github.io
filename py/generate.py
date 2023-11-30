#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jinja2
import os, sys

from pagedata import get_pagelist
from page import Page
import html_snippets
from utils import write_html_sep, get_file_date, get_html_from_markdown
from navbar import generate_navbar

output_dir = ".."


footer_template = None
body_template = None
header_template = None



def read_templates():
    """
    Read in the jinja templates.
    """
    global footer_template, body_template, header_template

    _header_file = "../templates/header_template.jinja.html"
    _body_file = "../templates/body_template.jinja.html"
    _footer_file = "../templates/footer_template.jinja.html"

    for f in [_header_file, _body_file, _footer_file]:
        if not os.path.exists(f):
            raise FileNotFoundError(f"Didn't find file '{f}'")

    fb= open(_body_file, "r")
    body_file = fb.read()
    fb.close()

    fh = open(_header_file, "r")
    header_file = fh.read()
    fh.close()

    ff = open(_footer_file, "r")
    footer_file = ff.read()
    ff.close()

    header_template = jinja2.Template(header_file)
    body_template = jinja2.Template(body_file)
    footer_template = jinja2.Template(footer_file)
    return


def get_maintext(page: Page):
    """
    Get maintext html from markdown file specified by `filename`.
    """
    return get_html_from_markdown(page.contentfile)


def get_header(page: Page):
    """
    Get html from markdown file specified by `filename`.
    """
    return "<!-- NO HEADER IN get_header() function -->"


def get_footer(page: Page):
    """
    Get html from markdown file specified by `filename`.
    """

    # we deal with the footer a bit differently because it needs
    # to go into the <body> of the html.

    vardict = page.get_vardict()
    footer = footer_template.render(**vardict)

    return footer



def setup_pages():
    """
    Set up the actual pages.
    """

    pages = get_pagelist()

    # Read in content
    for page in pages:

        page.DATE = get_file_date(page.contentfile)
        page.MAINTEXT = get_maintext(page)
        page.FOOTER = get_footer(page)

        if page.add_navbar:
            page.NAVIGATION_BAR = generate_navbar(page.outputfile)



    return pages




def generate_page(page: Page):
    """
    Generate a single page.

    page: class Page
    """

    output = page.outputfile
    fulloutputfile = os.path.join(output_dir, output)
    vardict = page.get_vardict()

    if output.endswith(".html"):
        print("Generating", fulloutputfile)
    else:
        print(f"{fulloutputfile} is not html file, skipping.")
        return

    f = open(fulloutputfile, "w", encoding="utf-8")

    f.write(html_snippets.html_start)

    html = header_template.render(**vardict)
    f.write(html)
    write_html_sep(f, "end header")

    html=body_template.render(**vardict)
    f.write(html)
    write_html_sep(f, "end body")

    f.close()

    return




if __name__ == "__main__":

    read_templates()
    pages = setup_pages()

    for page in pages:
        generate_page(page)
