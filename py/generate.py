#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  import jinja2
import os, sys

from pagedata import get_pagelist
from page import Page
import html_snippets
from utils import write_html_sep, get_html_from_markdown, read_template
from navbar import generate_navbar
from sidebar import generate_sidebar


output_dir = ".."

header_template_file = "../templates/header_template.jinja.html"
body_template_file = "../templates/body_template.jinja.html"
footer_template_file = "../templates/footer_template.jinja.html"


def get_footer(page: Page):
    """
    Generate the footer html.
    We deal with the footer a bit differently because it needs
    to go into the <body> of the html.
    """

    footer_template = read_template(footer_template_file)
    vardict = page.get_vardict()
    footer = footer_template.render(**vardict)
    page.FOOTER = footer
    return


def setup_pages():
    """
    Set up the actual pages.
    """

    pages = get_pagelist()

    # Read in content
    for page in pages:

        page.get_date()
        page.get_maintext()
        get_footer(page)

        if page.add_navbar:
            page.NAVIGATION_BAR = generate_navbar(page.outputfile)

        if page.add_sidebar:
            page.SIDEBAR = generate_sidebar(page)

    return pages


def generate_page(page: Page):
    """
    Generate a single page.

    page: class Page
    """

    header_template = read_template(header_template_file)
    body_template = read_template(body_template_file)
    footer_template = read_template(footer_template_file)

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

    html = body_template.render(**vardict)
    f.write(html)
    write_html_sep(f, "end body")

    f.close()

    return


if __name__ == "__main__":

    pages = setup_pages()

    for page in pages:
        generate_page(page)
