#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Page(object):
    """
    A base class containing page metadata of a single html page.
    """

    def __init__(self,
                 author: str = "Mladen Ivkovic",
                 date: str = "DATE_JINJA_ERROR",
                 title: str = "TITLE_JINJA_ERROR",
                 outputfile: str = "OUTPUT_NOT_PROVIDED",
                 contentfile: str = "content_file",
                 additional_header_content: str = "<!-- NO_EXTRA_HEADER_CONTENT --!>",
                 additional_footer_content: str = "<!-- NO_EXTRA_FOOTER_CONTENT --!>",
                 add_navbar: bool = True,
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

        self.MAINTEXT = "<!-- NO MAINTEXT -->"


        return


    def get_vardict(self) -> dict:
        """
        return a populated dict of all class attributes.
        """

        return self.__dict__


