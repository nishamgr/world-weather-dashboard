# weather-capstone

Project Overview:
- I decided to work on this World weather Website to scrape weather data using Selenium and Python. I aimed to scrape three things from data:
    1: City
    2- Weather_Condition
    3-Temperature
  
Project Elements:
. Python
. Pandas for data cleaning and transformation
. Chrome WebDriver for broser automation
. Selenium for web scraping
. CSV Files to store data
. Git and GitHub

Project Structure:
world-weather-daashboard/
..scrape_weather.py - Web Scraping script
..clean_weather.py - Data Cleaning script
..raw_weather.csv - Raw weather data
..cleaned_weather.csv - Cleaned weather data
..README.md - Project instructions

How to Run the Project:
1. Activate the Virtual Env
    - source .venv/bin/activate
2. Install Dependencies
    - pip install -r requirements.txt
3. Run Scraper
    - python src/scrape_weather.py
4. Run the Cleaning script
    - python src/clean_weather.py
        - this will create the cleaned_weather.csv data folder
Data Cleaning 
Clean the script
    - removes duplicate rows
    - saves the cleaned data to new CSV file

Challenges Faced
    - It was definitly identifying the correct HTML elements to scrape using Selenium. Also making sure that cleaning script was working correclty after troubleshooting the missing data. Eventually i was ablw to successfully scrape and clean the weather data.
