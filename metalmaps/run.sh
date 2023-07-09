#!/bin/bash

# Make sure to update all the colormap data in generate_html.py.
# generate_plots.py will then import all the colormaps from generate_html.py.

python3 ./generate_plots.py  && \
python3 ./generate_html.py > test.html
