#!/usr/bin/env python
# coding: utf-8

# Importing Libraries 

# In[10]:


import json
from datetime import datetime
import pandas as pd
import requests


# URL Information as well as API Key

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# 
# my api key is b019afe76634d8e3a0b5c322ec54a4d6
# 
# The url should look like this
# 
# https://api.openweathermap.org/data/2.5/weather?q=chattanooga&appid=b019afe76634d8e3a0b5c322ec54a4d6

# In[11]:


city_name = "Chattanooga"

base_url = "https://api.openweathermap.org/data/2.5/weather?q="

api_key = "b019afe76634d8e3a0b5c322ec54a4d6"


# In[12]:


#this is the full url but we can change the city name if we need
full_url = base_url + city_name + "&APPID=" + api_key


# In[14]:


#this tests the connection to the server. We are REQUESTING data from the server
r = requests.get(full_url)
print(r)


# In[15]:


#converting data to a json dictionary
data = r.json()
print(data)


# In[19]:


#converting kelvin to fahrenheit
def kelvin_to_fahrenheit(temp_in_kelvin):
    temp_in_fahrenheit = (temp_in_kelvin - 273.15) * (9/5) + 32
    return temp_in_fahrenheit


# In[20]:


#this is pulling the city name and ther information. Look back at the JSON libary and it says name (key): Chattanooga(list)
    city = data["name"]
    weather_description = data["weather"][0]['description']
    temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp"])
    feels_like_farenheit= kelvin_to_fahrenheit(data["main"]["feels_like"])
    min_temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp_min"])
    max_temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp_max"])
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    time_of_record = datetime.utcfromtimestamp(data['dt'] + data['timezone']) #brings back to local time
    sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])


# In[21]:


#putting data into a dictionary
    transformed_data = {"City": city,
                        "Description": weather_description,
                        "Temperature (F)": temp_farenheit,
                        "Feels Like (F)": feels_like_farenheit,
                        "Minimun Temp (F)":min_temp_farenheit,
                        "Maximum Temp (F)": max_temp_farenheit,
                        "Pressure": pressure,
                        "Humidty": humidity,
                        "Wind Speed": wind_speed,
                        "Time of Record": time_of_record,
                        "Sunrise (Local Time)":sunrise_time,
                        "Sunset (Local Time)": sunset_time                        
                        }


# In[23]:


transformed_data


# In[24]:


transformed_data_list = [transformed_data]
df_data = pd.DataFrame(transformed_data_list) #transforming to dataframe
# print(df_data)


# In[25]:


transformed_data_list


# In[26]:


df_data


# In[ ]:




