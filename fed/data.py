import pandas as pd
import requests


def download_gdp(start_year=2000, end_year=2022):
    """Download yearly GDP (current US$) from the World Bank API.

    Returns a dataframe with one row per year and one column per country.
    """
    wb_url = "https://api.worldbank.org/v2/country/{countries}/indicator/{indicator}"
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

    response = requests.get(
        wb_url.format(countries=";".join(countries), indicator=gdp_indicator),
        params={"format": "json", "date": f"{start_year}:{end_year}", "per_page": 1000},
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
    
    return df.pivot(index="year", columns="country", values="gdp")[
        list(countries.values())
    ].reset_index()

print(download_gdp(2000,2022))