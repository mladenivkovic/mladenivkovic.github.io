#!/usr/bin/env python3

import jinja2
from datetime import datetime


def cmapContainer(name, pretty_name, artist, art_url):

    return {
        "name": name,
        "pretty_name": pretty_name,
        "artist": artist,
        "url": art_url,
    }


viridis = cmapContainer(
    "viridis",
    "This is viridis",
    "alpha",
    "https://upload.wikimedia.org/wikipedia/en/d/da/Black_Sabbath_debut_album.jpg",
)
cividis = cmapContainer(
    "cividis",
    "This is cividis",
    "beta",
    "https://upload.wikimedia.org/wikipedia/en/d/da/Black_Sabbath_debut_album.jpg",
)
inferno = cmapContainer(
    "inferno",
    "This is inferno",
    "gamma",
    "https://upload.wikimedia.org/wikipedia/en/d/da/Black_Sabbath_debut_album.jpg",
)

mapCollection = [viridis, cividis, inferno]

# TODO: read version
version = "0.0.1"
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
