import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import plotly.express as px

st.title("World Weather Dashboard")

#load data
with sqlite3.connect("weather.db") as conn:
    df = pd.read_sql_query("SELECT * FROM cleaned_weather", conn)
    
#clean temp
df["Temperature"] = (
    df["Temperature"]
    .astype(str)
    .str.replace("°F", "", regex=False)
    .str.replace("°C", "", regex=False)
)

df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")
df = df.dropna(subset=["Temperature"])


required_cols = ["City", "Local_Time", "Temperature", "Weather_Condition"]
available_cols = [c for c in required_cols if c in df.columns]

#view
st.subheader("Weather Preview")
st.dataframe(df[available_cols].head())


#filter  
st.sidebar.header("Filters")

city = st.sidebar.selectbox("Select City", df["City"].unique())
filtered_df = df[df["City"] == city]

st.subheader(f"Weather for {city}")
st.dataframe(filtered_df[available_cols])

#time feature
if "Local_Time" in df.columns:
    df["Hour"] = df["Local_Time"].str.extract(r"(\d+)")
    df["Hour"] = pd.to_datetime(df["Local_Time"], errors="coerce")

#viz 1: weather type
st.subheader("Average Temperature by Time")
st.sidebar.header("Average Temperature by Time")

avg_temp = df.groupby("Local_Time")["Temperature"].mean().reset_index()

fig1 = px.bar(
    avg_temp,
    x="Local_Time",
    y="Temperature",
    labels={
        "Local_Time": "Local_Time",
        "Temperature": "Average Temperature"
    },
    color="Temperature"
)

st.plotly_chart(fig1, use_container_width=True)


#viz2: temp distrubution
st.sidebar.header("Temperature Distribution")
st.subheader("Temperature Distribution")

fig2 = px.histogram(
    df,
    x="Temperature",
    nbins=10,
    hover_data=["City", "Local_Time"]
)


st.plotly_chart(fig2, use_container_width=True)

#viz3: city comparision
st.sidebar.header("Avg. Temperature by City")
st.subheader("Temperature Comparison by City")

fig3 = px.box(
    df,
    x="City",
    y="Temperature",
)
st.plotly_chart(fig3, use_container_width=True)

