import pandas as pd
import sqlite3

#read csv file
raw_df = pd.read_csv("data/raw_weather.csv")
clean_df = pd.read_csv("data/cleaned_weather.csv")

#connecting to db
with sqlite3.connect("weather.db") as conn:
    raw_df.to_sql("raw_weather", conn, if_exists="replace", index=False)
    clean_df.to_sql("cleaned_weather", conn, if_exists="replace", index=False)
    
print("Data is loaded successfully.")