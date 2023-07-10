#!/usr/bin/env python3

# =================================================================================
# Show a plot of all colormaps with their names
#
# based on https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/
# =================================================================================

import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
import matplotlib as mpl

from mpl_toolkits.axes_grid1 import ImageGrid
from mpl_toolkits.axes_grid1 import Divider, Size

matplotlib.rcParams['font.family'] = 'monospace'
mpl.rcParams["figure.dpi"] = 100


from generate_html import mapCollection, plotAlbum
from metalmaps import *

def grayify_cmap(cmap):
    """Return a grayscale version of the colormap"""
    cmap = mpl.colormaps.get_cmap(cmap)

    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived greyscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return matplotlib.colors.LinearSegmentedColormap.from_list(
        cmap.name + "_grayscale", colors, cmap.N
    )


im = np.outer(np.ones(10), np.arange(100))


for mapdata in mapCollection:

    fig = plt.figure(figsize=(12, 0.9))

    name_ax = fig.add_subplot(2, 3, 1)
    color_ax = fig.add_subplot(2, 3, 2)
    color_ax_r = fig.add_subplot(2, 3, 3)
    empty_ax = fig.add_subplot(2, 3, 4)
    gray_ax = fig.add_subplot(2, 3, 5)
    gray_ax_r = fig.add_subplot(2, 3, 6)

    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.75, hspace=0.01, wspace=0.08)

    for ax in fig.axes:
        ax.axis("off")

    cmap_name = mapdata["name"]
    cmap = "metalmaps."+cmap_name

    title_font = {'fontname':'monospace', 'fontsize':10}
    artist_font = {'fontname':'DejaVu Sans', 'fontsize':12}

    color_ax.imshow(im, cmap=cmap)
    color_ax.set_title(cmap, **title_font)

    color_ax_r.imshow(im, cmap=cmap+"_r")
    color_ax_r.set_title(cmap+"_r", **title_font)

    gray_ax.imshow(im, cmap=grayify_cmap(cmap))
    gray_ax_r.imshow(im, cmap=grayify_cmap(cmap+"_r"))

    text = mapdata["pretty_name"] + " (" + mapdata["artist"] + ")"
    name_ax.text(0., 0., text, ha="left", va="center", **artist_font)
    name_ax.set_xlim(0, 1)
    name_ax.set_ylim(-1, 1)

    figname = "colormap-" + cmap_name + ".png"
    plt.savefig(figname, dpi=150)
    plt.close()

    break
