#!/usr/bin/env python3

import jinja2
from datetime import datetime
import metalmaps


def cmapContainer(name, pretty_name, artist, art_url):
    """
    Create a dict that can be used by jinja to generate the html.
    All arguments are strings.

    name: name of the colormap
    pretty_name: pretty name for the color map. Used in heading and table of contents.
    artist: artist name
    art_url: url to original album art to link on page.
    """

    return {
        "name": name,
        "pretty_name": pretty_name,
        "artist": artist,
        "url": art_url,
    }


red = cmapContainer(
    "red",
    "This is red",
    "alpha",
    "https://upload.wikimedia.org/wikipedia/en/d/da/Black_Sabbath_debut_album.jpg",
)

mapCollection = [red]

# TODO: read version
version = metalmaps.__version__
date = datetime.today().strftime("%Y-%m-%d")


if __name__ == "__main__":

    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    template = env.get_template("./metalmaps.html.jinja")

    print(
        template.render(
            cmaps=mapCollection,
            suffixes=["", "_r"],
            version=version,
            date=date,
        )
    )
