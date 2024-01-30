import pandas as pd

def data_2():
    country_raw = "https://raw.githubusercontent.com/rahilpacmann/case-data-wrangling-api/main/country.csv"
    country_df = pd.read_csv(country_raw)
    
    return country_df