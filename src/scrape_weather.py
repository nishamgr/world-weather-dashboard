from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get("https://www.timeanddate.com/weather/")

time.sleep(4)
#data scraping

#cities = driver.find_elements(
#    By.CLASS_NAME, "my-city_item"
#)

weather_data = []

#find the rows in the weather table/ prints num of rows sfound
rows = driver.find_elements(By.CSS_SELECTOR, "table.zebra.tb-theme tbody tr")
print("Cities found:", len(rows))

#looping thru each row
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    

    #checking rows/extracting text
    if len(cols) >= 4:
        city = cols[0].text
        weather = cols[1].text
        temp = cols[3].text
        
        weather_data.append([city, weather, temp])

#append rows to weather_data
df = pd.DataFrame(
    weather_data,
    columns=["City", "Weather_Condition", "Temperature"]
)
#Importing to CSV
df.to_csv("data/raw_weather.csv", index = False)

driver.quit()

