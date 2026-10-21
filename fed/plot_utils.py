import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from fed.data import download_gdp


def plot_gdp(start_year=2000, end_year=2022):
    """Plot GDP over time for the selected economies, one colour per country."""
    df = download_gdp(start_year, end_year).set_index("year")

    fig, ax = plt.subplots(figsize=(10, 6))
    colours = plt.get_cmap("tab10").colors
    for colour, country in zip(colours, df.columns):
        ax.plot(df.index, df[country], label=country, color=colour, linewidth=2)

    ax.set_xlabel("Year")
    ax.set_ylabel("GDP ($ Trillion)")
    ax.set_title(f"GDP ($ Trillion) in Selected Economies, {start_year}-{end_year}")
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
