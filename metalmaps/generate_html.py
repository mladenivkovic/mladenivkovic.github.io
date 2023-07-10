#!/usr/bin/env python3

import jinja2
from datetime import datetime
import metalmaps
from mapcollection import mapCollection


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
