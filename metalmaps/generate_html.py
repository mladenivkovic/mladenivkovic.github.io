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


apostasy = cmapContainer(
        "apostasy",
        "The Apostasy",
        "Behemoth",
        "https://coverartarchive.org/release/b9ca5e3c-a82c-3afd-ace3-cc4184723c52/2442134676.jpg"
        )

black_sabbath = cmapContainer(
    "black_sabbath",
    "Black Sabbath",
    "Black Sabbath",
    "https://coverartarchive.org/release/9fd196b4-0437-4ce2-9e7e-9966dfa86180/15612615429.jpg",
)

blues_brothers = cmapContainer(
        "blues_brothers",
        "The Blues Brothers",
        "The Blues Brothers",
        "https://coverartarchive.org/release/92be9637-0513-49cd-b9b6-5d9490599753/24708728971.jpg"
        )

blues_pills = cmapContainer(
        "blues_pills",
        "Blues Pills",
        "Blues Pills",
        "https://coverartarchive.org/release/97744fea-331a-4fcc-9476-69348cfa1364/17469949894.jpg"
        )

cosmos_factory = cmapContainer(
        "cosmos_factory",
        "Cosmo's Factory",
        "Creedence Clearwater Revival",
        "https://coverartarchive.org/release/067c3d38-1f5c-4596-baf3-e494a4342d1f/12385725136.jpg"
        )

london_calling = cmapContainer(
        "london_calling",
        "London Calling",
        "The Clash",
        "https://coverartarchive.org/release/7bec22a0-eb73-4b79-a619-b253d5c2af87/4527734511.jpg"
        )

master_of_puppets = cmapContainer(
        "master_of_puppets",
        "Master of Puppets",
        "Metallica",
        "https://coverartarchive.org/release/cb100c18-fb29-4828-8d24-2fdbac6d6cff/8600878942.jpg"
        )



meteora = cmapContainer(
        "meteora",
        "Meteora",
        "Linkin Park",
        "https://coverartarchive.org/release/dd5fd2b3-576e-4354-bc67-68e6f006fd26/3167538307.jpg"
        )

obzen = cmapContainer(
        "obzen",
        "obZen",
        "Meshuggah",
        "https://coverartarchive.org/release/fa7028f6-d4ac-4b4c-b87f-7c042d1b5c80/10833262918.jpg"
        )

paranoid = cmapContainer(
        "paranoid",
        "Paranoid",
        "Black Sabbath",
        "https://coverartarchive.org/release/d820f080-845a-4525-8e46-087ce9f8cdda/23423100131.jpg"
        )

ride_the_lightning = cmapContainer(
        "ride_the_lightning",
        "Ride the Lightning",
        "Metallica",
        "https://coverartarchive.org/release/589ff96d-0be8-3f82-bdd2-299592e51b40/15674886619.jpg"
        )

ziggy_stardust = cmapContainer(
        "ziggy_stardust",
        "The Rise and Fall of Ziggy Stardust and the Spiders From Mars",
        "David Bowie",
        "https://coverartarchive.org/release/bb7f0f5a-586e-3f90-8665-fdc547aa2a54/1239299887.jpg"
        )

deep_purple_in_rock = cmapContainer(
        "deep_purple_in_rock",
        "Deep Purple in Rock",
        "Deep Purple",
        "https://coverartarchive.org/release/5156ea9f-eb54-4258-bbf0-e3af9219de1f/31715408459.jpg"
        )

made_in_japan = cmapContainer(
        "made_in_japan",
        "Made in Japan",
        "Deep Purple",
        "https://coverartarchive.org/release/fb49386f-541a-4928-a606-1f6c9aacaec5/5977807803.jpg"
        )

dethalbum = cmapContainer(
        "dethalbum",
        "The Dethalbum",
        "Dethklok",
        "https://coverartarchive.org/release/5379197a-54bf-45f5-95fe-f995fd047d50/19745544468.jpg"
        )

la_woman = cmapContainer(
        "la_woman",
        "L.A. Woman",
        "The Doors",
        "https://coverartarchive.org/release/e68f23df-61e3-4264-bfc3-17ac3a6f856b/5132812481.jpg"
        )

from_mars_to_sirius = cmapContainer(
        "from_mars_to_sirius",
        "From Mars to Sirius",
        "Gojira",
        "https://coverartarchive.org/release/6ea45c08-3cfa-461a-aa4d-4cc404fcfa86/1512690278.jpg"
        )


plotAlbum = from_mars_to_sirius

mapCollection = [
            apostasy,
            black_sabbath,
            blues_brothers,
            blues_pills,
            cosmos_factory,
            deep_purple_in_rock,
            dethalbum,
            from_mars_to_sirius,
            la_woman,
            london_calling,
            master_of_puppets,
            made_in_japan,
            meteora,
            obzen,
            paranoid,
            ride_the_lightning,
            ziggy_stardust,
        ]



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
