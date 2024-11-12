#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re

from utils import (
    get_file_date,
    get_html_from_markdown,
    extract_anchor_and_name_from_heading,
)


class Page(object):
    """
    A base class containing page metadata of a single html page.
    """

    def __init__(
        self,
        author: str = "Mladen Ivkovic",
        date: str = "DATE_JINJA_ERROR",
        title: str = "TITLE_JINJA_ERROR",
        outputfile: str = "OUTPUT_NOT_PROVIDED",
        contentfile: str = "content_file",
        additional_header_content: str = "<!-- NO_EXTRA_HEADER_CONTENT --!>",
        additional_footer_content: str = "<!-- NO_EXTRA_FOOTER_CONTENT --!>",
        add_navbar: bool = True,
        add_sidebar: bool = False,
    ) -> None:
        """
        author: str
            author name

        date: str
            date of last change in page

        title: str
            title of the page

        outputfile: str
            html output file name

        contentfile: str
            markdown file name to read content from

        """

        self.AUTHOR = author
        self.DATE = date
        self.TITLE = title

        self.outputfile = outputfile
        self.contentfile = contentfile

        self.ADDITIONAL_HEADER_CONTENT = additional_header_content
        self.ADDITIONAL_FOOTER_CONTENT = additional_footer_content

        self.add_navbar = add_navbar
        self.NAVIGATION_BAR = "<!-- NO NAVIGATION BAR -->"

        self.add_sidebar = add_sidebar
        self.SIDEBAR = "<!-- NO SIDE BAR -->"

        self.MAINTEXT = "<!-- NO MAINTEXT -->"
        self.FOOTER = "<!-- NO FOOTER -->"

        self.got_maintext = False

        return

    def get_vardict(self) -> dict:
        """
        return a populated dict of all class attributes.
        """

        return self.__dict__

    def get_maintext(self):
        """
        Get maintext html from markdown file specified by `filename`.
        """
        self.MAINTEXT = get_html_from_markdown(self.contentfile)
        self.got_maintext = True
        return

    def get_date(self):
        """
        Get the last modified date of the file using git.
        """
        self.DATE = get_file_date(self.contentfile)
        return

    def get_toc_entries(self):
        """
        Extract the Table of Contents entries and anchors and heading levels
        from the maintext.
        """

        if not self.got_maintext:
            raise ValueError(
                "Trying to extract ToC entries without having read maintext."
            )

        # grab all headings
        soup = BeautifulSoup(self.MAINTEXT, "html.parser")
        headings = soup.find_all(re.compile("h[1-5]"))

        anchors = []
        names = []
        levels = []

        for head in headings:
            anchor, name, level = extract_anchor_and_name_from_heading(
                head, self.contentfile
            )
            if anchor is not None and name is not None:
                anchors.append(anchor)
                names.append(name)
                levels.append(level)

        return anchors, names, levels
