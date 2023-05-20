import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
#import matplotlib.pyplot as plt
import numpy as np
#import plotly.express as px
import altair as alt
import math
import requests
import json

# Title
st.title('Space Data')

#Definition
st.write("This app displays the current number of astronauts in space, their name and the position of the ISS station in the world")

#Load astronauts data
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()

#Number of people
if response.status_code == 200:
    number_of_people = data["number"]
    st.write("Number of people in space is:", number_of_people)
else:
    st.write("Error: Unable to fetch data")

#Name of people
if response.status_code == 200:
    astronauts = data["people"]
    st.write("Astronauts currently in space:")
    
    col1, col2 = st.columns(2)  # Create two columns
    
    for i, astronaut in enumerate(astronauts):
        if i % 2 == 0:  # Place astronaut name in alternating columns
            col1.write("- " + astronaut["name"])
        else:
            col2.write("- " + astronaut["name"])
else:
    st.write("Error: Unable to fetch data")

#load iss data
url_iss = "http://api.open-notify.org/iss-now.json"
response_iss = requests.get(url_iss)
data_iss = response_iss.json()

#create map
if response_iss.status_code == 200:
    iss_location = {
        'latitude': [float(data_iss["iss_position"]["latitude"])],
        'longitude': [float(data_iss["iss_position"]["longitude"])]
    }
    df = pd.DataFrame(iss_location)
    st.map(df)
    st.write("Current ISS Location:")
    st.write("Latitude:", data_iss["iss_position"]["latitude"])
    st.write("Longitude:", data_iss["iss_position"]["longitude"])
else:
    st.write("Error: Unable to fetch data")