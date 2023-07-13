#!/usr/bin/env python3

"""
A collection of all metalmaps color maps with some extra data.
"""


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


animals = cmapContainer(
    "animals",
    "Animals",
    "Pink Floyd",
    "https://coverartarchive.org/release/b249399e-77a7-3bb5-ba51-7368506e6f02/8215817116.jpg",
)

apostasy = cmapContainer(
    "apostasy",
    "The Apostasy",
    "Behemoth",
    "https://coverartarchive.org/release/b9ca5e3c-a82c-3afd-ace3-cc4184723c52/2442134676.jpg",
)

ashes_of_the_wake = cmapContainer(
    "ashes_of_the_wake",
    "Ashes of the Wake",
    "Lamb of God",
    "https://coverartarchive.org/release/6012b20e-8fdd-4afc-9b0e-a9f22bce81a1/36090160874.jpg",
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
    "https://coverartarchive.org/release/92be9637-0513-49cd-b9b6-5d9490599753/24708728971.jpg",
)

blues_pills = cmapContainer(
    "blues_pills",
    "Blues Pills",
    "Blues Pills",
    "https://coverartarchive.org/release/97744fea-331a-4fcc-9476-69348cfa1364/17469949894.jpg",
)

cosmos_factory = cmapContainer(
    "cosmos_factory",
    "Cosmo's Factory",
    "Creedence Clearwater Revival",
    "https://coverartarchive.org/release/067c3d38-1f5c-4596-baf3-e494a4342d1f/12385725136.jpg",
)

fear_of_the_dark = cmapContainer(
    "fear_of_the_dark",
    "Fear of the Dark",
    "Iron Maiden",
    "https://coverartarchive.org/release/ecc2e9db-637c-4f21-955c-6ab3e1123ffc/1282374549.jpg",
)

from_mars_to_sirius = cmapContainer(
    "from_mars_to_sirius",
    "From Mars to Sirius",
    "Gojira",
    "https://coverartarchive.org/release/6ea45c08-3cfa-461a-aa4d-4cc404fcfa86/1512690278.jpg",
)

deep_purple_in_rock = cmapContainer(
    "deep_purple_in_rock",
    "Deep Purple in Rock",
    "Deep Purple",
    "https://coverartarchive.org/release/5156ea9f-eb54-4258-bbf0-e3af9219de1f/31715408459.jpg",
)

dethalbum = cmapContainer(
    "dethalbum",
    "The Dethalbum",
    "Dethklok",
    "https://coverartarchive.org/release/5379197a-54bf-45f5-95fe-f995fd047d50/19745544468.jpg",
)

hybrid_theory = cmapContainer(
    "hybrid_theory",
    "Hybrid Theory",
    "Linkin Park",
    "https://coverartarchive.org/release/a17a48b6-51db-3c52-8fdd-066fb9989f78/33576269845.jpg",
)

hypnotize = cmapContainer(
    "hypnotize",
    "Hypnotize",
    "System of a Down",
    "https://coverartarchive.org/release/c5c36cb2-d409-4c97-ae21-9f331a895566/29540284142.jpg",
)

in_utero = cmapContainer(
    "in_utero",
    "In Utero",
    "Nirvana",
    "https://coverartarchive.org/release/80189394-8ca0-4a97-9d0e-aad32725de22/32188969568.jpg",
)

la_woman = cmapContainer(
    "la_woman",
    "L.A. Woman",
    "The Doors",
    "https://coverartarchive.org/release/e68f23df-61e3-4264-bfc3-17ac3a6f856b/5132812481.jpg",
)

lenfant_sauvage = cmapContainer(
    "lenfant_sauvage",
    "L'enfant Sauvage",
    "Gojira",
    "https://coverartarchive.org/release/5b7e9d43-8330-4f91-8e78-81dde869e9b5/16931897915.jpg",
)

london_calling = cmapContainer(
    "london_calling",
    "London Calling",
    "The Clash",
    "https://coverartarchive.org/release/7bec22a0-eb73-4b79-a619-b253d5c2af87/4527734511.jpg",
)

made_in_japan = cmapContainer(
    "made_in_japan",
    "Made in Japan",
    "Deep Purple",
    "https://coverartarchive.org/release/fb49386f-541a-4928-a606-1f6c9aacaec5/5977807803.jpg",
)

master_of_puppets = cmapContainer(
    "master_of_puppets",
    "Master of Puppets",
    "Metallica",
    "https://coverartarchive.org/release/cb100c18-fb29-4828-8d24-2fdbac6d6cff/8600878942.jpg",
)

meteora = cmapContainer(
    "meteora",
    "Meteora",
    "Linkin Park",
    "https://coverartarchive.org/release/dd5fd2b3-576e-4354-bc67-68e6f006fd26/3167538307.jpg",
)

number_of_the_beast = cmapContainer(
    "number_of_the_beast",
    "The Number of the Beast",
    "Iron Maiden",
    "https://coverartarchive.org/release/5aa782e6-d87a-3ec1-af46-ff68c76cf8fc/7847268318.jpg",
)

obzen = cmapContainer(
    "obzen",
    "obZen",
    "Meshuggah",
    "https://coverartarchive.org/release/fa7028f6-d4ac-4b4c-b87f-7c042d1b5c80/10833262918.jpg",
)

overkill = cmapContainer(
    "overkill",
    "Overkill",
    "Mot&oumlrhead",
    "https://coverartarchive.org/release/a7b33578-a44a-47e8-bcb8-e1ba8eb848fc/9157237778.jpg",
)

painkiller = cmapContainer(
    "painkiller",
    "Painkiller",
    "Judas Priest",
    "https://coverartarchive.org/release/f3228f88-1315-4f7e-9c68-2acf0d2f6e90/7356437148.jpg",
)

paranoid = cmapContainer(
    "paranoid",
    "Paranoid",
    "Black Sabbath",
    "https://coverartarchive.org/release/d820f080-845a-4525-8e46-087ce9f8cdda/23423100131.jpg",
)

powerslave = cmapContainer(
    "powerslave",
    "Powerslave",
    "Iron Maiden",
    "https://coverartarchive.org/release/4766bf83-3b58-4584-b75a-43917627b790/2595131402.jpg",
)

rage_against_the_machine = cmapContainer(
    "rage_against_the_machine",
    "Rage Against The Machine",
    "Rage Against The Machine",
    "https://coverartarchive.org/release/20fd2c8f-671c-4ebe-921b-39204dde8f89/14831559261.jpg",
)

reign_in_blood = cmapContainer(
    "reign_in_blood",
    "Reign in Blood",
    "Slayer",
    "https://coverartarchive.org/release/f09a3d0b-5760-41e5-bd62-1e7403b27522/26676279934.jpg",
)

ride_the_lightning = cmapContainer(
    "ride_the_lightning",
    "Ride the Lightning",
    "Metallica",
    "https://coverartarchive.org/release/589ff96d-0be8-3f82-bdd2-299592e51b40/15674886619.jpg",
)

rock_n_roll = cmapContainer(
    "rock_n_roll",
    "Rock 'n' Roll",
    "Mot&oumlrhead",
    "https://coverartarchive.org/release/b4bdc9c6-a3c0-4e50-a6f5-fe6ec5e66609/14298490837.jpg",
)

screaming_for_vengeance = cmapContainer(
    "screaming_for_vengeance",
    "Screaming for Vengeance",
    "Judas Priest",
    "https://coverartarchive.org/release/57e2798e-d7d0-4250-a17b-0b8fb56ade4f/11916137754.jpg",
)

south_of_heaven = cmapContainer(
    "south_of_heaven",
    "South of Heaven",
    "Slayer",
    "https://coverartarchive.org/release/407ade2e-03b4-3951-b244-b97de8fb0433/7844026684.jpg",
)

the_hunter = cmapContainer(
    "the_hunter",
    "The Hunter",
    "Mastodon",
    "https://coverartarchive.org/release/e349eaf2-865c-4b47-b719-29d4b5f8e789/3586926524.jpg",
)

ziggy_stardust = cmapContainer(
    "ziggy_stardust",
    "The Rise and Fall of Ziggy Stardust and the Spiders From Mars",
    "David Bowie",
    "https://coverartarchive.org/release/bb7f0f5a-586e-3f90-8665-fdc547aa2a54/1239299887.jpg",
)

plotAlbum = hybrid_theory

mapCollection = [
    animals,
    apostasy,
    ashes_of_the_wake,
    black_sabbath,
    blues_brothers,
    blues_pills,
    cosmos_factory,
    deep_purple_in_rock,
    dethalbum,
    fear_of_the_dark,
    from_mars_to_sirius,
    hybrid_theory,
    hypnotize,
    in_utero,
    la_woman,
    lenfant_sauvage,
    london_calling,
    master_of_puppets,
    made_in_japan,
    meteora,
    number_of_the_beast,
    obzen,
    overkill,
    painkiller,
    paranoid,
    powerslave,
    reign_in_blood,
    ride_the_lightning,
    rock_n_roll,
    screaming_for_vengeance,
    south_of_heaven,
    the_hunter,
    ziggy_stardust,
    rage_against_the_machine,
]

# Sort maps by name.
_mapnames = [c["name"] for c in mapCollection]
tuples = sorted(zip(_mapnames, mapCollection))
mapCollection = [t[1] for t in tuples]
