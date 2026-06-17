import pandas as pd

#read the raw_weather data
df = pd.read_csv("data/raw_weather.csv")

df.columns = df.columns.str.strip()

print(df.head())
print(df.columns)

print("This is before cleaning:")
print(df.shape)

#removes any dupes rows
df = df.drop_duplicates()

print("This is after removing dups")
print(df.shape)

#transformation to remove extra spaces from cities name
df["City"] = df["City"].str.strip()
print("This is after cleaning:")
print(df.shape)

#To keep rows with only cities names
df = df[df["City"].notna()]

print("This is after cleaning:")
print(df.shape)

#removing missing vals
#df = df.dropna()
#print("After removing missing vals:")

#saves the clean data
df.to_csv("data/cleaned_weather.csv", index=False)
print("Finished!")