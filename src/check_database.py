import pandas as pd
import sqlite3

with sqlite3.connect("weather.db") as conn:
    df = pd.read_sql_query(
        "SELECT * FROM cleaned_weather LIMIT 5;",
        conn
    )
print(df)