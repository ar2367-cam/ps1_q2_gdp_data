import pandas as pd
import requests


def download_gdp(start_year: int = 2000, end_year: int = 2022) -> pd.DataFrame:
    """Download yearly GDP (current US$) from the World Bank API.

    Returns a dataframe with one row per year and one column per country.
    """
    wb_base = "https://api.worldbank.org/v2"
    wb_url = wb_base + "/country/{countries}/indicator/{indicator}"
    gdp_indicator = "NY.GDP.MKTP.CD"  # GDP, current US$
    countries = {
        "GBR": "United Kingdom",
        "USA": "United States",
        "BRA": "Brazil",
        "JPN": "Japan",
        "CHN": "China",
        "DEU": "Germany",
        "CHE": "Switzerland",
    }

    params: dict[str, str | int] = {
        "format": "json",
        "date": f"{start_year}:{end_year}",
        "per_page": 1000,
    }
    response = requests.get(
        wb_url.format(countries=";".join(countries), indicator=gdp_indicator),
        params=params,
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if len(payload) < 2 or payload[1] is None:
        raise ValueError(f"World Bank API returned no data: {payload[0]}")

    df = pd.DataFrame(
        {
            "year": int(row["date"]),
            "country": countries[row["countryiso3code"]],
            "gdp": row["value"],
        }
        for row in payload[1]
    )

    df["gdp"] = df["gdp"] / 1e12  # convert US$ to trillions of US$

    return (
        df.pivot(index="year", columns="country", values="gdp")[
            list(countries.values())
        ]
        .rename_axis(columns=None)
        .reset_index()
    )


print(download_gdp(2000, 2022))
