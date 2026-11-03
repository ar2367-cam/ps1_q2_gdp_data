import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

from fed.data import download_gdp


def plot_gdp(
    start_year: int = 2000,
    end_year: int = 2022,
) -> tuple[Figure, Axes]:
    """Plot GDP over time for the selected economies, one colour each."""
    df = download_gdp(start_year, end_year).set_index("year")

    fig, ax = plt.subplots(figsize=(10, 6))
    cmap = plt.get_cmap("tab10")
    colours = [cmap(i) for i in range(cmap.N)]
    for colour, country in zip(colours, df.columns):
        ax.plot(
            df.index,
            df[country],
            label=country,
            color=colour,
            linewidth=2,
        )

    ax.set_xlabel("Year")
    ax.set_ylabel("GDP ($ Trillion)")
    ax.set_title(
        f"GDP ($ Trillion) in Selected Economies, {start_year}-{end_year}",
    )
    ax.set_xlim(start_year, end_year)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(title="Country", frameon=True, edgecolor="black")

    fig.tight_layout()
    return fig, ax


if __name__ == "__main__":
    plot_gdp()
    plt.show()
