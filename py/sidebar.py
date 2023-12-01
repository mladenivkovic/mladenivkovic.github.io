#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jinja2
from page import Page

# side bar jinja template
_sidebar_template_file = "../templates/sidebar.jinja.html"


class TocItem(object):
    """
    An object to store side bar (table of contents) metadata.
    """

    def __init__(self, anchor:str, name:str, level:int):
        """
        anchor: anchor to link to
        name: name of ToC entry
        level: heading level. E.g. 3 for <h3>
        """

        self.anchor = anchor
        self.name = name
        self.level = level

        self.is_last = False
        self.closing_count = 0
        self.indent = False
        self.unindent = False

        return





def generate_sidebar(page: Page):
    """
    Generate sidebar (table of contents) html for a page.
    specified by the page name.
    """

    sf = open(_sidebar_template_file, "r")
    tocfile = sf.read()
    sf.close()

    template = jinja2.Template(tocfile)

    anchors, names, levels = page.get_toc_entries()
    toc_item_list = []

    if len(names) == 0:
        print(f"WARNING: Didn't find any headings in file '{page.contentfile}'")
        print("WARNING: Skipping side bar creation")
        print("*****")

        sidebar = "<!-- NO SIDEBAR; FOUND NO HEADINGS IN SOURCE FILE -->"
        return sidebar


    minlevel = min(levels)

    for i in range(len(names)):
        new = TocItem(anchors[i], names[i], levels[i])

        if i > 0:
            # if heading level increased, mark down that we indent
            # the entry in the table of contents
            if levels[i-1] < levels[i]:
                new.indent = True

        if i < len(names) - 1:
            # if heading level decreases, mark down that we un-indent
            # the entry in the table of contents
            if levels[i] > levels[i+1]:
                new.unindent = True

        toc_item_list.append(new)

    # mark down the last entry as special.
    toc_item_list[-1].is_last = True
    # we might need to close up some </ul>.
    toc_item_list[-1].closing_count = toc_item_list[-1].level - minlevel

    sidebar = template.render(toc_list=toc_item_list)

    return sidebar


