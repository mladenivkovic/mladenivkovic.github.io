#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jinja2

# navigation bar jinja template
_navbar_template_file = "../templates/navigation_bar.jinja.html"


class NavItem(object):
    """
    An object to store navigation bar metadata.
    """

    def __init__(self, filename:str, title:str, name:str):
        """
        filename: name of file navigation bar links to.
        title: title of page navbar links to. What you will see in the navigation bar.
        name: internal name of page.
        """

        self.filename = filename
        self.title = title
        self.name = name

        return



_nav_home = NavItem("index.html", "Home", "home")
_nav_work = NavItem("work.html", "My Work", "work")
_nav_cv = NavItem("CV.html", "CV", "cv")
_nav_scripts = NavItem("scripts-and-summaries.html", "Scripts and Study Material", "scripts")
_nav_software = NavItem("software.html", "Software", "software")
_nav_gallery = NavItem("gallery.html", "Gallery", "gallery")
_nav_links = NavItem("links.html", "Links", "links")
_nav_personal = NavItem("personal.html", "Personal", "personal")


# Stick all navigation items in this list. Order matters.
_nav_item_list = [
                    _nav_home,
                    _nav_work,
                    _nav_cv,
                    _nav_scripts,
                    _nav_software,
                    _nav_gallery,
                    _nav_links,
                    _nav_personal,
        ]



def generate_navbar(pagename):
    """
    Generate navigation bar html for a specific html file
    specified by the page name.
    """

    nf = open(_navbar_template_file, "r")
    navfile = nf.read()
    nf.close()

    template = jinja2.Template(navfile)

    navbar = template.render(nav_list=_nav_item_list, pagename=pagename)
    return navbar


