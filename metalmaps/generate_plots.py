#!/usr/bin/env python3

import matplotlib as mpl
from matplotlib import pyplot as plt

from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker
import h5py
import numpy as np
import os
from mapcollection import mapCollection, plotAlbum
import metalmaps

outputdir = "images"


# Plot parameters
params = {
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "font.size": 9,
    "font.family": "serif",
    "figure.figsize": (5, 5),
    "figure.dpi": 100,
}
mpl.rcParams.update(params)


def add_colorbar(im, ax, fig):
    """
    add a nice colorbar to the plot which has the same size
    as the plot. Remove all ticks and labels from the colorbar.

    im: the image

    ax: the axis object you plotted on

    fig: the pyplot figure to work on
    """
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(im, cax=cax)
    cbar.set_ticks([])
    cbar.set_ticklabels([])
    return


def savefig(cmap, plot, ax):
    """
    Save figure.

    cmap: which colormap this is. String.
    plot: which data we're plotting. E.g. "EAGLE", or "KH", or "NGC". String.
    ax: which axis we're working with.
    """

    if not os.path.exists(outputdir):
        os.mkdir(outputdir)

    filename = plot + "-" + cmap + ".jpg"
    fullfilename = os.path.join(outputdir, filename)
    plt.sca(ax)
    plt.savefig(fullfilename, dpi=300)
    print("Saved", fullfilename)
    plt.close()


def make_EAGLE_plot(cmap):
    """
    Make a plot using the EAGLE data.
    """

    srcfile = "mass_plots_eagle25.hdf5"

    hfile = h5py.File(srcfile, "r")

    rhoDM = hfile["dm_mass_map"][:]
    rhoDM = rhoDM / rhoDM.max()  # scale down to [0,1]
    rho = hfile["mass_map"][:]
    rho = rho / rho.max()  # scale down to [0,1]

    # make halt plot DM, half plot baryon
    rhoPlot = rhoDM[:]
    rhoPlot[:, rho.shape[0] // 2 :] = rho[:, rho.shape[0] // 2 :]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(
        np.log10(rhoPlot),
        origin="lower",
        extent=(0, 1, 0, 1),
        #  norm = LogNorm(), # LogNorm fucks with the colorbar ticks?!?! So skip it.
        cmap=cmap,
    )

    add_colorbar(im, ax, fig)
    title = r"EAGLE 25"

    ax.set_title(title)
    ax.set_xlabel(r"x", usetex=True)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_ylabel(r"y", usetex=True)
    ax.set_yticks([])
    ax.set_yticklabels([])
    plt.tight_layout()
    savefig(cmap, "EAGLE", ax)


def make_KH_plot(cmap):
    """
    Make a plot using the Kelvin-Helmholtz data.
    """

    srcfile = "kelvin-helmholtz.hdf5"

    hfile = h5py.File(srcfile, "r")
    data = hfile["data"]
    rho = data["density"]

    metadata = hfile["metadata"]
    time = metadata.attrs["time"]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(
        np.log10(rho),
        origin="lower",
        extent=(0, 1, 0, 1),
        #  norm = LogNorm(), # LogNorm fucks with the colorbar ticks?!?! So skip it.
        cmap=cmap,
    )

    add_colorbar(im, ax, fig)
    title = r"$t = {0:.3f}$".format(time)

    ax.set_title(title)
    ax.set_xlabel(r"x", usetex=True)
    ax.set_ylabel(r"y", usetex=True)
    plt.tight_layout()
    savefig(cmap, "KH", ax)

    return


def make_NGC_plot(cmap):
    """
    Make a plot using the NGC image.
    """

    srcfile = "NGC7496.hdf5"

    hfile = h5py.File(srcfile, "r")

    rho = hfile["image"][:]
    rho = rho / rho.max()  # scale down to [0,1]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(
        rho,
        extent=(0, 1, 0, 1),
        #  norm = LogNorm(), # LogNorm fucks with the colorbar ticks?!?! So skip it.
        cmap=cmap,
    )

    add_colorbar(im, ax, fig)
    title = r"NGC7496"

    ax.set_title(title)
    ax.set_xlabel(r"x", usetex=True)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_ylabel(r"y", usetex=True)
    ax.set_yticks([])
    ax.set_yticklabels([])
    plt.tight_layout()
    savefig(cmap, "NGC", ax)

    return


# for line plots
x = np.linspace(0, 1.4, 200)

# for line plots
def y(x, phi):
    return np.sin(1.2 * np.pi * (x + 0.25) - 0.1 * phi)


def make_lineplot(cmap) :
    """
    Make a line plot.
    """

    metalmaps.set_color_cycle(cmap)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for i in range(10):
        col = "C"+str(i)
        cmap_colnames = metalmaps.colorcycle.get_colorlist_from_colormap(cmap)
        #  cmap_colnames = "#000000"
        plt.plot(x, y(x, i), lw=3, c=col, label=col+" - "+cmap_colnames[i])

    ax.set_xlabel(r"x", usetex=True)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_ylabel(r"y", usetex=True)
    ax.set_yticks([])
    ax.set_yticklabels([])

    plt.legend(ncols=2, fontsize="small", loc="upper right")
    plt.tight_layout()
    savefig(cmap, "lineplot", ax)



if __name__ == "__main__":
    #  cmaps = ["metalmaps." + c["name"] for c in [plotAlbum]]
    cmaps = ["metalmaps." + c["name"] for c in mapCollection]
    for cmap in cmaps:
        for suffix in ["", "_r"]:
            c = cmap + suffix
            make_KH_plot(c)
            make_EAGLE_plot(c)
            make_NGC_plot(c)
            make_lineplot(c)
