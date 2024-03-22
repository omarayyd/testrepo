#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import numpy as np
import datetime

# Setting this option will print all collumns of a dataframe
pd.set_option('display.max_columns', None)
# Setting this option will print all of the data in a feature
pd.set_option('display.max_colwidth', None)


# In[3]:


def getBoosterVersion(data):
    for x in data['rocket']:
       if x:
        response = requests.get("https://api.spacexdata.com/v4/rockets/"+str(x)).json()
        BoosterVersion.append(response['name'])


# In[66]:


r1= requests.get("https://api.spacexdata.com/v4/rockets/"+"5e9d0d95eda69955f709d1eb").json()
r1


# In[4]:


def getLaunchSite(data):
    for x in data['launchpad']:
       if x:
         response = requests.get("https://api.spacexdata.com/v4/launchpads/"+str(x)).json()
         Longitude.append(response['longitude'])
         Latitude.append(response['latitude'])
         LaunchSite.append(response['name'])


# In[5]:


def getPayloadData(data):
    for load in data['payloads']:
       if load:
        response = requests.get("https://api.spacexdata.com/v4/payloads/"+load).json()
        PayloadMass.append(response['mass_kg'])
        Orbit.append(response['orbit'])


# In[6]:


def getCoreData(data):
    for core in data['cores']:
            if core['core'] != None:
                response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
                Block.append(response['block'])
                ReusedCount.append(response['reuse_count'])
                Serial.append(response['serial'])
            else:
                Block.append(None)
                ReusedCount.append(None)
                Serial.append(None)
            Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
            Flights.append(core['flight'])
            GridFins.append(core['gridfins'])
            Reused.append(core['reused'])
            Legs.append(core['legs'])
            LandingPad.append(core['landpad'])


# In[7]:


spacex_url="https://api.spacexdata.com/v4/launches/past"


# In[8]:


response = requests.get(spacex_url)


# In[9]:


print(response.content)


# In[11]:


static_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'


# In[13]:


response = requests.get(static_json_url)


# In[14]:


response.status_code


# In[15]:


print(response.content)


# In[20]:


json_response =response.json()


# In[24]:


df=pd.json_normalize(json_response)


# In[25]:


df


# In[26]:


df=df[['rocket', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']]


# In[33]:


df=df[df["cores"].map(len)==1]
df=df[df["payloads"].map(len)==1]


# In[34]:


df


# In[36]:


df['cores'] = df['cores'].map(lambda x : x[0])
df['payloads'] = df['payloads'].map(lambda x : x[0])


# In[37]:


df


# In[43]:


df['date'] = pd.to_datetime(df['date_utc']).dt.date


# In[44]:


df


# In[46]:


df = df[df['date'] <= datetime.date(2020, 11, 13)]
df


# In[47]:


BoosterVersion = []
PayloadMass = []
Orbit = []
LaunchSite = []
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []
Block = []
ReusedCount = []
Serial = []
Longitude = []
Latitude = []


# In[54]:


getBoosterVersion(df)


# In[50]:


BoosterVersion[0:5]


# In[68]:


getLaunchSite(df)
getPayloadData(df)
getCoreData(df)


# In[70]:


launch_dict = {'FlightNumber': list(df['flight_number']),
'Date': list(df['date']),
'BoosterVersion':BoosterVersion,
'PayloadMass':PayloadMass,
'Orbit':Orbit,
'LaunchSite':LaunchSite,
'Outcome':Outcome,
'Flights':Flights,
'GridFins':GridFins,
'Reused':Reused,
'Legs':Legs,
'LandingPad':LandingPad,
'Block':Block,
'ReusedCount':ReusedCount,
'Serial':Serial,
'Longitude': Longitude,
'Latitude': Latitude}


# In[84]:


len(launch_dict["BoosterVersion"])


# In[85]:


BoosterVersion=[]
getBoosterVersion(df)


# In[86]:


len(BoosterVersion)


# In[87]:


launch_dict = {'FlightNumber': list(df['flight_number']),
'Date': list(df['date']),
'BoosterVersion':BoosterVersion,
'PayloadMass':PayloadMass,
'Orbit':Orbit,
'LaunchSite':LaunchSite,
'Outcome':Outcome,
'Flights':Flights,
'GridFins':GridFins,
'Reused':Reused,
'Legs':Legs,
'LandingPad':LandingPad,
'Block':Block,
'ReusedCount':ReusedCount,
'Serial':Serial,
'Longitude': Longitude,
'Latitude': Latitude}


# In[103]:


new_df=pd.DataFrame.from_dict(launch_dict)


# In[104]:


new_df.describe()


# In[105]:


data_falcon9=new_df[new_df["BoosterVersion"] == "Falcon 9"]


# In[106]:


data_falcon9


# In[107]:


data_falcon9["FlightNumber"]=range(1,91)


# In[108]:


data_falcon9["FlightNumber"]


# In[109]:


data_falcon9


# In[114]:


data_falcon9.isnull().sum()


# In[117]:


data_falcon9.columns


# In[120]:


data_falcon9["PayloadMass"].replace(np.nan,data_falcon9["PayloadMass"].mean(),inplace= True)


# In[121]:


data_falcon9.isnull().sum()


# In[ ]:




