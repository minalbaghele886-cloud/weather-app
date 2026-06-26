import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(
    page_title="weather application",
    page_icon="🌤️"
)

st.title("⛅weather application")
st.write("enter your city name and click the button to get the weather data")

city = st.text_input("enter the city name")
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

if st.button("Fetch weather data"):
   response = requests.get(API_URL)
   if response.status_code == 200:
     st.success("data fetched successfully")
     data = response.json()

     name = data["name"]
     country = data["sys"]["country"]
     st.subheader(f"weather data for {name}, {country}")

     temp = data["main"]["temp"]
     humidity = data["main"]["humidity"] 
     wind_speed = data["wind"]["speed"]
     weather = data["weather"][0]["main"]

     col1, col2, col3, col4 = st.columns(4)

     col1.metric("temperature",f"🌡️{temp}°C")
     col2.metric("humidity",f"💧{humidity}%")
     col3.metric("wind speed",f"🍃{wind_speed} m/s")
     col4.metric("weather condition",f"⛅{weather}")
   else:
      st.error("invalid city name")



