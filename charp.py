"""
CharP is Charts for Paulo — Paulos aux functions and preferences for beautiful
and functional charts
"""

import matplotlib as mpl
import matplotlib.pyplot as plt


plt.style.use("./paulo.mplstyle")

color_highlight = plt.rcParams["lines.color"]  # default is orange
color_highlight2 = (0, 153, 51)
color_highlight3 = (30, 66, 139)


def set_title(title, fontsize=16, ax=None):
    "Title always aligned to the left axis label"
    # https://stackoverflow.com/questions/62997001/matplotlib-how-to-exact-align-the-title-to-the-y-label
    if ax is None:
        ax = plt.gca()
    plt.gcf().canvas.draw()  # without this, it won't work
    x_min = min(lb.get_window_extent().x0 for lb in ax.get_yticklabels())
    x_min = min(mpl.text.Text.get_window_extent(lb).x0 for lb in ax.get_yticklabels())
    x, _ = ax.transAxes.inverted().transform([x_min, 0])
    plt.gcf().canvas.draw()  # without this, it won't work
    return ax.set_title(title, ha="left", x=x, fontsize=fontsize)


def rotate_xlabels(angle=45):
    plt.tick_params(axis="x", labelrotation=angle, ha="right")


def barh(ax=None):
    if ax is None:
        ax = plt.gca()
    # label on top
    ax.tick_params(
        axis="x",
        top=False,
        labeltop=True,
        bottom=False,
        labelbottom=False,
        pad=-13,  # hardcoded looks wrong
    )
    # white grid
    ax.grid(axis="x", color="white", linestyle="--")
    ax.grid(False, axis="y")
    ax.set_axisbelow(False)

    # spines
    ax.spines["bottom"].set_visible(False)
    # identar à direita?


def bar(ax=None):
    if ax is None:
        ax = plt.gca()
    # white grid
    ax.grid(axis="y", color="white", linestyle="dotted")
    ax.set_axisbelow(False)

    ax.tick_params(
        axis="x", bottom=False,
    )


def example_chart():
    # in ipython type: %matplotlib
    import seaborn as sns

    df = sns.load_dataset("iris")
    fig = plt.figure()
    ax = fig.gca()
    plt.plot(df.query('species=="virginica"').petal_length)
    ax.set_title("Maria vai com as outras")
    return ax
