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
            outputfile="gallery.html",
            contentfile="../content/gallery.md",
            add_navbar=True,
            add_sidebar=True,
            )

    scripts = Page(
            author="Mladen Ivkovic",
            title="Manuscripts, Summaries, and Study Material",
            outputfile="scripts-and-summaries.html",
            contentfile="../content/scripts-and-summaries.md",
            add_navbar=True,
            add_sidebar=True,
            )

    work = Page(
            author="Mladen Ivkovic",
            title="My Work",
            outputfile="work.html",
            contentfile="../content/work.md",
            add_navbar=True,
            add_sidebar=True,
            )

    cv = Page(
            author="Mladen Ivkovic",
            title="CV",
            outputfile="CV.html",
            contentfile="../content/cv.md",
            add_navbar=True,
            add_sidebar=False,
            )

    links = Page(
            author="Mladen Ivkovic",
            title="Links",
            outputfile="links.html",
            contentfile="../content/links.md",
            add_navbar=True,
            add_sidebar=False,
            )

    my_name = Page(
            author="Mladen Ivkovic",
            title="My Name",
            outputfile="my_name.html",
            contentfile="../content/my_name.md",
            add_navbar=True,
            add_sidebar=False,
            )



    # Add all pages to a list, which you return.
    # The order shouldn't matter.
    pages = [
            mainpage,
            software,
            gallery,
            scripts,
            work,
            cv,
            links,
            my_name,
         ]

    return pages

