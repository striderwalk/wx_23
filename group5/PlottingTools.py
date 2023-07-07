import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.animation as anim
import math


def plot(
    x,
    y,
    ax,
    scatter=False,
    xlbl="x",
    ylbl="y",
    lbl=None,
    bar=False,
    bins=None,
    xmax=None,
    xmin=None,
    ymax=None,
    ymin=None,
):
    """
    takes an axes and data as parameters and plots the axes
    if bar = true a bar graph plotted instead
    """
    if x is None:
        x = np.linspace(-0.5, 10.5, 2200)
    # sets the grid for the data
    ax.grid(which="both", ls=":", lw=0.5)
    ax.set_xlabel(xlbl)
    ax.set_ylabel(ylbl)
    if ax is None:
        ax = plt.gca()
    # if the bar parameter is true
    if bar:
        bars = []
        # splits the y data into arrays
        data = np.array_split(y, bins)
        x = np.linspace(-0.5, 10.5, bins)
        # iterate over the 2d array data
        for i in data:
            count = 0
            total = 0
            for j in i:
                count = count + 1
                total = total + j
            bars.append(total / count)
        # plots the bar graph
        ax.bar(x, bars, label=lbl)

        return ax

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    if scatter:
        ax.scatter(x, y)
    else:
        ax.plot(x, y, label=lbl)

    return ax


def figure(rows=1, columns=1, figSize=(10, 5)):
    """
    creates a figure and gridspec for that figure and returns them
    make sure to keep the two variables together
    """
    fig = plt.figure(figsize=figSize, constrained_layout=True)
    spec = gridspec.GridSpec(ncols=columns, nrows=rows, figure=fig)
    return fig, spec


def makeAxes(fig, spec, index, twoy=False, zlbl="Y2"):
    """
    Parameters:
    fig = the figure you want to add the axes to
    spec = the layout of the fig that you are using
    twoY = if you want two y axes on the graph, if true the function will return a graph with 2 y axes
    also passes in all of the axes labels
    """
    # xList = fig.axes
    # index = len(axList)

    # if index == (spec.ncols*spec.nrows):
    #     if spec.ncols == spec.nrows:
    #         spec = gridspec.GridSpec(ncols=(spec.ncols+1),nrows=spec.nrows,figure=fig)
    #     else:
    #         spec = gridspec.GridSpec(ncols=(spec.ncols),nrows=(spec.nrows+1),figure=fig)

    # print(spec.get_geometry)
    # for x in range(len(axList)-1):
    #     print(axList[x])
    #     print(spec[x])
    #     axList[x].set_position(spec[x])

    ax = fig.add_subplot(spec[index])
    # sets the axes labels

    # checks if there should be 2 y axes
    if twoy:
        ax2 = plt.twinx(ax)
        # sets the y label
        ax2.set_ylabel(zlbl)
        # returns 2 axes
        return ax, ax2
    return ax


def makeErrorBar(ax, x, y, bar):
    """
    pass in an axes object
    pass in x and y data
    graph must be plotted beforehand
    pass in the error amount
    """
    if ax is None:
        ax = plt.gca()
    ax.fill_between(
        x, y - bar, y + bar, alpha=0.5, edgecolor="#CC4F1B", facecolor="#FF9848"
    )
    return ax
