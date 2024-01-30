import pandas as pd

def data_1():
    city_raw = "https://raw.githubusercontent.com/rahilpacmann/case-data-wrangling-api/main/city.csv"
    city_df = pd.read_csv(city_raw)
    
    return city_df