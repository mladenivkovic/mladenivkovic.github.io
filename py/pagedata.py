#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==================================================
# defines a list of pages using the Page class, and
# fills them up with correct metadata.
# ==================================================


from page import Page


def get_pagelist():
    """
    Generate the list of html pages to generate.
    """

    mainpage = Page(
            author="Mladen Ivkovic",
            title="Mladen Ivkovic's Home Page",
            outputfile="index.html",
            contentfile="../content/index.md",
            add_navbar=True,
            add_sidebar=False,
            )

    software = Page(
            author="Mladen Ivkovic",
            title="Software",
            outputfile="software.html",
            contentfile="../content/software.md",
            add_navbar=True,
            add_sidebar=False,
            )

    gallery = Page(
            author="Mladen Ivkovic",
            title="Gallery",
            outputfile="gallery_new.html",
            contentfile="../content/gallery.md",
            add_navbar=True,
            add_sidebar=True,
            )


    # Add all pages to a list, which you return.
    # The order shouldn't matter.
    pages = [
            mainpage,
            software,
            gallery,
         ]

    return pages

