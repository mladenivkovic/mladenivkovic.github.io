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

    def __init__(self, anchor:str, name:str):
        """
        anchor: anchor to link to
        name: name of ToC entry
        """

        self.anchor = anchor
        self.name = name

        return





def generate_sidebar(page: Page):
    """
    Generate sidebar (table of contents) html for a page.
    specified by the page name.
    """

    nf = open(_sidebar_template_file, "r")
    tocfile = nf.read()
    nf.close()

    template = jinja2.Template(tocfile)

    anchors, names = page.get_toc_entries()
    toc_item_list = []
    for i in range(len(names)):
        new = TocItem(anchors[i], names[i])
        toc_item_list.append(new)


    sidebar = template.render(toc_list=toc_item_list)

    return sidebar


