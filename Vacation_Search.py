#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd
import requests
import gmaps

# Import API key
from config import g_key

# Configure gmaps
gmaps.configure(api_key=g_key)


# In[ ]:


# 1. Read the WeatherPy_vacation.csv into a DataFrame.
vacation_df = pd.read_csv("Vacation_Search/WeatherPy_vacation.csv")
vacation_df.head()


# In[3]:


# 2. Using the template add the city name, the country code, the weather description and maximum temperature for the city.
info_box_template = """
<dl>
<dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
<dt>Max Temp</dt><dd>{Max Temp} °F</dd>
<dt>Current Description</dt><dd>{Current Description}</dd>
</dl>
"""

# 3a. Get the data from each row and add it to the formatting template and store the data in a list.
hotel_info = [info_box_template.format(**row) for index, row in clean_hotel_df.iterrows()]

# 3b. Get the latitude and longitude from each row and store in a new DataFrame.
locations = clean_hotel_df[["Lat", "Lng"]]


# In[ ]:


# 4a. Add a marker layer for each city to the map.
fig = gmaps.figure(center=(30.0, 30.0), zoom_level=1.5)
marker_layer = gmaps.marker_layer(locations, info_box_content=hotel_info)
fig.add_layer(marker_layer)
# 4b. Display the figure
fig


# In[ ]:


# From the map above pick 4 cities and create a vacation itinerary route to travel between the four cities. 
# 5. Create DataFrames for each city by filtering the 'vacation_df' using the loc method. 
# Hint: The starting and ending city should be the same city.

vacation_start = vacation_df.loc[]
vacation_end = vacation_df.loc[]
vacation_stop1 = vacation_df.loc[]
vacation_stop2 = vacation_df.loc[] 
vacation_stop3 = vacation_df.loc[] 


# In[ ]:


# 6. Get the latitude-longitude pairs as tuples from each city DataFrame using the to_numpy function and list indexing.
start = tuple(vacation_start[["Lat","Lng"]].to_numpy()[0])
end = tuple(vacation_end[["Lat","Lng"]].to_numpy()[0])
stop1 = tuple(vacation_stop1[["Lat","Lng"]].to_numpy()[0])
stop2 = tuple(vacation_stop2[["Lat","Lng"]].to_numpy()[0])
stop3 = tuple(vacation_stop3[["Lat","Lng"]].to_numpy()[0])


# In[ ]:


# 7. Create a direction layer map using the start and end latitude-longitude pairs,
# and stop1, stop2, and stop3 as the waypoints. The travel_mode should be "DRIVING", "BICYCLING", or "WALKING".
fig = gmaps.figure()
ways_route = gmaps.ways_layer(start, end,waypoints=[stop1, stop2, stop3], 
                                           travel_mode="DRIVING","BICYCLING", "WALKING")

fig.add_layer(ways_route)
fig


# In[ ]:


# 8. To create a marker layer map between the four cities.
#  Combine the four city DataFrames into one DataFrame using the concat() function.
itinerary_df = pd.concat([vacation_start,vacation_stop1,vacation_stop2,vacation_stop3],ignore_index=True)
itinerary_df


# In[ ]:


# 9 Using the template add city name, the country code, the weather description and maximum temperature for the city. 
info_box_template = """
<dl>
<dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
<dt>Max Temp</dt><dd>{Max Temp} °F</dd>
<dt>Current Description</dt><dd>{Current Description}</dd>
</dl>"""

# 10a Get the data from each row and add it to the formatting template and store the data in a list.
hotel_info = [info_box_template.format(**row) for index, row in itinerary_df.iterrows()]

# 10b. Get the latitude and longitude from each row and store in a new DataFrame.
locations = itinerary_df[["Lat", "Lng"]]


# In[ ]:


# 11a. Add a marker layer for each city to the map.
fig = gmaps.figure()
marker_layer = gmaps.marker_layer(locations, info_box_content=hotel_info)
fig.add_layer(marker_layer)
# 11b. Display the figure
fig

