#!/usr/bin/env python
# coding: utf-8

# ### Author: Akshay Ijantkar
# ### Team: Aqua Wizards
# ### Project: Surfers Bible

# * https://launchschool.com/books/sql/read/table_relationships

# # Import Libraries:

# In[ ]:


# waterTemperature,wavePeriod,waveDirection,waveHeight,windWaveDirection,windWaveHeight,windWavePeriod,swellPeriod,secondarySwellPeriod,swellDirection,secondarySwellDirection,swellHeight,secondarySwellHeight,windSpeed,windSpeed20m,windSpeed30m,windSpeed40m,windSpeed50m,windSpeed80m,windSpeed100m,windSpeed1000hpa,windSpeed800hpa,windSpeed500hpa,windSpeed200hpa,windDirection,windDirection20m,windDirection30m,windDirection40m,windDirection50m,windDirection80m,windDirection100m,windDirection1000hpa,windDirection800hpa,windDirection500hpa,windDirection200hpa,airTemperature,airTemperature80m,airTemperature100m,airTemperature1000hpa,airTemperature800hpa,airTemperature500hpa,airTemperature200hpa,precipitation,gust,cloudCover,humidity,pressure,visibility,currentSpeed,currentDirection,iceCover,snowDepth,seaLevel


# In[1]:


import pandas as pd
import numpy as np
import random
import matplotlib as plt
from matplotlib import pyplot
# import seaborn as sns; sns.set()
# from scipy.stats import norm 
import matplotlib.pyplot as plt
# For Linear regression
# from sklearn.linear_model import LinearRegression
# For split given dataset into train and test set.
# from sklearn.model_selection import train_test_split
# To verify models using this metrics 
# from sklearn.metrics import mean_squared_error, r2_score

# import statsmodels.formula.api as smf
# from sklearn.linear_model import LinearRegression
# from sklearn import metrics
# v
from matplotlib import rcParams
rcParams['figure.figsize'] = 50,50
import pandas_profiling
pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from pandas import ExcelWriter
from pandas import ExcelFile

from pygeocoder import Geocoder

import sys
from weather_au import api
from weather_au import summary
from weather import place, observations, uv_index
import time

import json
import requests
from datetime import datetime, timedelta
# from catboost import CatBoostClassifier
# from sklearn.model_selection import train_test_split

# from sklearn.metrics import r2_score
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.wrappers.scikit_learn import KerasRegressor
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import KFold
# from sklearn.model_selection import cross_validate

# import catboost as ctb
# from catboost import CatBoostRegressor, FeaturesData, Pool
# from scipy.stats import uniform as sp_randFloat
# from scipy.stats import randint as sp_randInt
# from scipy.stats import uniform
# from sklearn.model_selection import RandomizedSearchCV
# from sklearn.metrics.pairwise import cosine_similarity
# from  sklearn.metrics.pairwise import euclidean_distances
# from sklearn.metrics.pairwise import manhattan_distances
# from sklearn.metrics.pairwise import pairwise_distances
import re
import pprint
from datetime import date
import datetime
import sqlite3
from sqlite3 import Error
from datetime import datetime
from dateutil import tz
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# # Give Date:

# In[53]:


from datetime import datetime
import datetime
no_days_from_today = 3

select_date = ""

if select_date == "":    
    today = date.today()
    given_date = today.strftime("%Y-%m-%d") 
    given_date =  str((datetime.datetime.strptime(given_date, "%Y-%m-%d") + datetime.timedelta(days = no_days_from_today)).date())
    
else:
    given_date = select_date
    
given_date    
# given_datetime


# # Import Beach Table to DF: 

# In[3]:


import psycopg2 as ps

# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'test-surfers-bible-instance.cljoljhkgpfb.ap-southeast-2.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : 5432, # change to your port
               'POSTGRES_USERNAME' : 'ai_postgres', # change to your username
               'POSTGRES_PASSWORD' : 'postgres2309', # change to your password
               'POSTGRES_DBNAME' : 'test_surfers_bible_db'} # change to your db name

# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])

cur = conn.cursor()

beach_df = pd.read_sql_query("SELECT * FROM BEACH_TABLE;", conn)

conn.close()
cur.close()

# beach_df.head()


# # API KEYS:

# In[27]:


SG_API_KEY_DICT = {}
SG_API_KEY_DICT['1'] = "8aab844c-8cfd-11ea-9f57-0242ac130002-8aab8500-8cfd-11ea-9f57-0242ac130002"
SG_API_KEY_DICT['2'] = "ca3fa016-8cfd-11ea-ad84-0242ac130002-ca3fa0c0-8cfd-11ea-ad84-0242ac130002"
SG_API_KEY_DICT['3'] = "f4171838-8cfd-11ea-8581-0242ac130002-f41718ec-8cfd-11ea-8581-0242ac130002"
SG_API_KEY_DICT['4'] = "79c117d6-8cfe-11ea-be46-0242ac130002-79c11894-8cfe-11ea-be46-0242ac130002"

SG_API_KEY_DICT['5'] = "2c7dcffe-8cff-11ea-b78d-0242ac130002-2c7dd0a8-8cff-11ea-b78d-0242ac130002"
SG_API_KEY_DICT['6'] = "aefa9c5a-8cff-11ea-b78d-0242ac130002-aefa9d04-8cff-11ea-b78d-0242ac130002"
SG_API_KEY_DICT['7'] = "adb63958-945c-11ea-af71-0242ac130002-adb63a2a-945c-11ea-af71-0242ac130002"
SG_API_KEY_DICT['8'] = "f0cc6ae6-945c-11ea-84c3-0242ac130002-f0cc6b9a-945c-11ea-84c3-0242ac130002"

SG_API_KEY_DICT['9'] = "16e74080-9461-11ea-84c3-0242ac130002-16e7418e-9461-11ea-84c3-0242ac130002"
SG_API_KEY_DICT['10'] = "678f70b6-9461-11ea-af71-0242ac130002-678f7160-9461-11ea-af71-0242ac130002"
SG_API_KEY_DICT['11'] = "b6144834-9460-11ea-af71-0242ac130002-b614494c-9460-11ea-af71-0242ac130002"
SG_API_KEY_DICT['12'] = "62b0ff58-945f-11ea-94e2-0242ac130002-62b10070-945f-11ea-94e2-0242ac130002"

SG_API_KEY_DICT['test'] = "7d624590-7b4c-11ea-9892-0242ac130002-7d624644-7b4c-11ea-9892-0242ac130002"


# # UTILITY FUNCTIONS:

# In[6]:


def get_unix_time_epochs(datetime_str):
    return int(time.mktime(time.strptime(str(datetime_str), '%Y-%m-%dT%H:%M:%S')))


# In[7]:


def convert_datetime_in_dif_timezones(from_datetime_str, from_timezone_str, to_timezone_str, 
                                      datetime_format = '%Y-%m-%dT%H:%M:%S'):
#     USE pytz.all_timezones to get all timestamps
    from datetime import datetime
    import pytz
    date_time_obj = datetime.strptime(from_datetime_str, datetime_format)
#     print("date_time_obj = ", date_time_obj)
    
    old_timezone = pytz.timezone(from_timezone_str)
    new_timezone = pytz.timezone(to_timezone_str)
    
    new_timezone_timestamp = old_timezone.localize(date_time_obj).astimezone(new_timezone).strftime("%Y-%m-%dT%H:%M:%S") 
#     print("new_timezone_timestamp", new_timezone_timestamp)
    return str(new_timezone_timestamp)
    


# # SEA_WATER_QUALITY DATA:

# In[ ]:


bio_col_lst = [  
                'date',
                'beach_id',
                'beach_name',
                'beach_latitude',
                'beach_longitude',
                'beach_state',    
                "beach_municipality",
    
                 'chlorophyll',
                 'iron',
                 'nitrate',
                 'oxygen',
                 'ph',
                 'phosphate',
                 'phyto',
                 'phytoplankton',
                 'salinity',
                 'silicate',
                 'time'
                ]

bio_df = pd.DataFrame(columns = bio_col_lst
                         )
# bio_df


# # SEA_WATER_QUALITY: API CALLS:

# In[ ]:


# %%time
# Wall time: 5min 34s
import datetime
for api_limit, api_no in zip(range(0,200,50) ,range(1,5)):
    print("++++++++++++++++++++++++++++++++++++++++++++")
    API_KEY = SG_API_KEY_DICT[str(api_no)]
    print("api_limit = ", api_limit)
    print("api_no = ", api_no)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    
    for index, row in beach_df.loc[api_limit  : api_limit + 50,].iterrows():
        print("")
        print("index = ", index)
        print("beach_name", row["beach_name"])
        print(" ")

        latitude = row['beach_latitude']
        longitude = row['beach_longitude']

        start_date = given_date
        end_date = str((datetime.datetime.strptime(given_date, "%Y-%m-%d") + datetime.timedelta(days = 1)).date())

        url_str = "https://api.stormglass.io/v2/bio/point?"
        url_str += "lat="+ str(latitude) +"&"
        url_str += "lng="+str(longitude) + "&"
        url_str += "start=" + start_date + "&"
        url_str += "end="+ end_date + "&"
        url_str += "params=iron,nitrate,chlorophyll,phyto,oxygen,ph,phytoplankton,phosphate,silicate,salinity"

        payload = {}
        headers = {
          'Authorization': API_KEY
        }

        response = requests.request("GET", url_str, headers=headers, data = payload)
        response_dict = json.loads(response.text)    
    #     print("response_dict = ", response_dict)
        bio_dict = {}

        for hour_dict in response_dict['hours']:
    #         print("hour_dict = ", hour_dict)

            bio_dict['date'] = given_date
            for beach_col in beach_df.columns.tolist():
                bio_dict[beach_col] = row[beach_col]     

            bio_col_lst = list(hour_dict.keys())
            bio_col_lst.remove("time")

            for bio_col in bio_col_lst:

                bio_dict[bio_col] = hour_dict[bio_col]['sg']

            bio_dict['time'] = hour_dict['time']

            bio_df = bio_df.append(bio_dict, ignore_index=True)
###################################################################################################################


# # CONVERT UTC TIME TO AUSTRALIA TIME:

# In[ ]:


bio_df['time'] = bio_df['time'].apply(lambda x: convert_datetime_in_dif_timezones(from_datetime_str = x, 
                                                                                  from_timezone_str = 'UTC', 
                                                                                  to_timezone_str ='Australia/Melbourne', 
                                                                                datetime_format = '%Y-%m-%dT%H:%M:%S+00:00'))


# # CREATE SEA_WATER_QUALITY_TABLE:

# In[ ]:


import psycopg2 as ps

# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'test-surfers-bible-instance.cljoljhkgpfb.ap-southeast-2.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : 5432, # change to your port
               'POSTGRES_USERNAME' : 'ai_postgres', # change to your username
               'POSTGRES_PASSWORD' : 'postgres2309', # change to your password
               'POSTGRES_DBNAME' : 'test_surfers_bible_db'} # change to your db name

# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])

cur = conn.cursor()

# cur.execute("DROP TABLE SEA_WATER_QUALITY_TABLE;")

create_table_query = '''
      CREATE TABLE IF NOT EXISTS SEA_WATER_QUALITY_TABLE
      (
        sea_water_quality_id SERIAL PRIMARY KEY,
        date DATE,
        beach_id INTEGER,
        beach_name TEXT,
        beach_latitude REAL,
        beach_longitude REAL,
        beach_state  TEXT,
        beach_municipality TEXT,
        chlorophyll REAL,
        iron REAL,
        nitrate REAL,
        oxygen REAL,
        ph REAL,
        phosphate REAL,
        phyto REAL,
        phytoplankton REAL,
        salinity REAL,
        silicate REAL,
        time TEXT,
        FOREIGN KEY (beach_id) REFERENCES beach_table(beach_id) ON DELETE CASCADE
       ); 
       '''

cur.execute(create_table_query)
conn.commit()


# # INSERT SEA_WATER_QUALITY_TABLE:

# In[ ]:


# %%time
# Wall time: 12min 51s
import psycopg2 as ps

# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'test-surfers-bible-instance.cljoljhkgpfb.ap-southeast-2.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : 5432, # change to your port
               'POSTGRES_USERNAME' : 'ai_postgres', # change to your username
               'POSTGRES_PASSWORD' : 'postgres2309', # change to your password
               'POSTGRES_DBNAME' : 'test_surfers_bible_db'} # change to your db name

# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])

cur = conn.cursor()

fill_question_mark_str = str(tuple(["%s"  for i in bio_df.columns.tolist()])).replace("'", "")
fill_question_mark_str

for row in bio_df.itertuples():
    data_tuple = tuple(row[1:])

    print("data_tuple = ", data_tuple)
    print(" ")
    
    cur.execute("""
                        INSERT INTO SEA_WATER_QUALITY_TABLE
                        (
                            date,
                            beach_id,
                            beach_name,
                            beach_latitude,
                            beach_longitude,
                            beach_state,
                            beach_municipality,
                            chlorophyll,
                            iron,
                            nitrate,
                            oxygen,
                            ph,
                            phosphate,
                            phyto,
                            phytoplankton,
                            salinity,
                            silicate,
                            time
                         ) VALUES  
                         """ + fill_question_mark_str + " ;"
                , data_tuple)    

conn.commit()
cur.close()
conn.close()


# ___
# ___
# ___

# # SWELL DATA:

# # SWELL: API CALLS:

# In[12]:


swell_col_lst = [
    'date',
    'beach_id',
    'beach_name',
    'beach_latitude',
    'beach_longitude',
    'beach_state',    
    "beach_municipality",
    
    'airTemperature',
    'cloudCover',
    'currentDirection',
    'currentSpeed',
    'gust',
    'humidity',
    'precipitation',
    'pressure',
    'seaLevel',
    'secondarySwellDirection',
    'secondarySwellHeight',
    'secondarySwellPeriod',
    'swellDirection',
    'swellHeight',
    'swellPeriod',
    'time',
    'visibility',
    'waterTemperature',
    'waveDirection',
    'waveHeight',
    'wavePeriod',
    'windDirection',
    'windSpeed',
    'windWaveDirection',
    'windWaveHeight',
    'windWavePeriod'
]
swell_df = pd.DataFrame(columns = swell_col_lst
                         )
# swell_df


# In[13]:


# %%time
# Wall time: 5min 48s
import datetime
for api_limit, api_no in zip(range(0,200,50) ,range(5,9)):
    print("++++++++++++++++++++++++++++++++++++++++++++")
    API_KEY = SG_API_KEY_DICT[str(api_no)]
    print("SWELL: api_limit = ", api_limit)
    print("api_no = ", api_no)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    
    for index, row in beach_df.loc[api_limit  : api_limit + 50,].iterrows():
        print("")
        print("index = ", index)
        print("beach_name", row["beach_name"])
        print(" ")

        latitude = row['beach_latitude']
        longitude = row['beach_longitude']

        start_date = given_date
        end_date = str((datetime.datetime.strptime(given_date, "%Y-%m-%d") + datetime.timedelta(days = 1)).date())

        url_str = "https://api.stormglass.io/v2/weather/point?"
        url_str += "lat="+ str(latitude) +"&"
        url_str += "lng="+str(longitude) + "&"
        url_str += "start=" + start_date + "&"
        url_str += "end="+ end_date + "&"
        url_str += "params=waterTemperature,wavePeriod,waveDirection,waveHeight,windWaveDirection,windWaveHeight,windWavePeriod,swellPeriod,secondarySwellPeriod,swellDirection,secondarySwellDirection,swellHeight,secondarySwellHeight,windSpeed,windDirection,airTemperature,precipitation,gust,cloudCover,humidity,pressure,visibility,currentSpeed,currentDirection,seaLevel"

        payload = {}
        headers = {
          'Authorization': API_KEY
        }

        response = requests.request("GET", url_str, headers=headers, data = payload)
        response_dict = json.loads(response.text)    
    #     print("response_dict = ", response_dict)
        swell_dict = {}

        for hour_dict in response_dict['hours']:
    #         print("hour_dict = ", hour_dict)

            swell_dict['date'] = given_date
            for beach_col in beach_df.columns.tolist():
                swell_dict[beach_col] = row[beach_col]     

            swell_col_lst = list(hour_dict.keys())
            swell_col_lst.remove("time")

            for swell_col in swell_col_lst:

                swell_dict[swell_col] = hour_dict[swell_col]['sg']

            swell_dict['time'] = hour_dict['time']

            swell_df = swell_df.append(swell_dict, ignore_index=True)
###################################################################################################################


# # CONVERT UTC TIME TO AUSTRALIA TIME:

# In[16]:


swell_df['time'] = swell_df['time'].apply(lambda x: convert_datetime_in_dif_timezones(from_datetime_str = x, 
                                                                                  from_timezone_str = 'UTC', 
                                                                                  to_timezone_str ='Australia/Melbourne', 
                                                                                datetime_format = '%Y-%m-%dT%H:%M:%S+00:00'))


# # CREATE SEA_WATER_QUALITY_TABLE:

# In[19]:


import psycopg2 as ps

# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'test-surfers-bible-instance.cljoljhkgpfb.ap-southeast-2.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : 5432, # change to your port
               'POSTGRES_USERNAME' : 'ai_postgres', # change to your username
               'POSTGRES_PASSWORD' : 'postgres2309', # change to your password
               'POSTGRES_DBNAME' : 'test_surfers_bible_db'} # change to your db name

# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])

cur = conn.cursor()

# cur.execute("DROP TABLE SEA_WATER_QUALITY_TABLE;")

create_table_query = '''
      CREATE TABLE IF NOT EXISTS SWELL_TABLE
      (
        swell_id SERIAL PRIMARY KEY,
        date DATE,
        beach_id INTEGER,
        beach_name TEXT,
        beach_latitude REAL,
        beach_longitude REAL,
        beach_state TEXT,
        beach_municipality TEXT,
        airTemperature REAL,
        cloudCover REAL,
        currentDirection REAL,
        currentSpeed REAL,
        gust REAL,
        humidity REAL,
        precipitation REAL,
        pressure REAL,
        seaLevel REAL,
        secondarySwellDirection REAL,
        secondarySwellHeight REAL,
        secondarySwellPeriod REAL,
        swellDirection REAL,
        swellHeight REAL,
        swellPeriod REAL,
        time TEXT,
        visibility REAL,
        waterTemperature REAL,
        waveDirection REAL,
        waveHeight REAL,
        wavePeriod REAL,
        windDirection REAL,
        windSpeed REAL,
        windWaveDirection REAL,
        windWaveHeight REAL,
        windWavePeriod REAL,
        FOREIGN KEY (beach_id) REFERENCES beach_table(beach_id) ON DELETE CASCADE
       ); 
       '''

cur.execute(create_table_query)
conn.commit()


# # INSERT SEA_WATER_QUALITY_TABLE:

# In[20]:


# %%time
# Wall time: 12min 51s
import psycopg2 as ps

# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'test-surfers-bible-instance.cljoljhkgpfb.ap-southeast-2.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : 5432, # change to your port
               'POSTGRES_USERNAME' : 'ai_postgres', # change to your username
               'POSTGRES_PASSWORD' : 'postgres2309', # change to your password
               'POSTGRES_DBNAME' : 'test_surfers_bible_db'} # change to your db name

# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])

cur = conn.cursor()

fill_question_mark_str = str(tuple(["%s"  for i in swell_df.columns.tolist()])).replace("'", "")
fill_question_mark_str

for row in swell_df.itertuples():
    data_tuple = tuple(row[1:])

    print("data_tuple = ", data_tuple)
    print(" ")
    
    cur.execute("""
                        INSERT INTO SWELL_TABLE
                        (
                            date,
                            beach_id,
                            beach_name,
                            beach_latitude,
                            beach_longitude,
                            beach_state,
                            beach_municipality,
                            airTemperature,
                            cloudCover,
                            currentDirection,
                            currentSpeed,
                            gust,
                            humidity,
                            precipitation,
                            pressure,
                            seaLevel,
                            secondarySwellDirection,
                            secondarySwellHeight,
                            secondarySwellPeriod,
                            swellDirection,
                            swellHeight,
                            swellPeriod,
                            time,
                            visibility,
                            waterTemperature,
                            waveDirection,
                            waveHeight,
                            wavePeriod,
                            windDirection,
                            windSpeed,
                            windWaveDirection,
                            windWaveHeight,
                            windWavePeriod
                         ) VALUES  
                         """ + fill_question_mark_str + " ;"
                , data_tuple)    

conn.commit()
cur.close()
conn.close()


# # ASTRONOMICAL DATA:

# # astronomy: API CALLS:

# In[36]:


astronomy_col_lst = [
    'date',
    'beach_id',
    'beach_name',
    'beach_latitude',
    'beach_longitude',
    'beach_state',    
    "beach_municipality",
    
    'astronomicalDawn',
     'astronomicalDusk',
     'civilDawn',
     'civilDusk',
     'moonFraction',
     'moonPhase',
     'moonrise',
     'moonset',
     'nauticalDawn',
     'nauticalDusk',
     'sunrise',
     'sunset',
     'time'
]
astronomy_df = pd.DataFrame(columns = astronomy_col_lst
                         )
astronomy_df


# In[37]:


# %%time
# Wall time: 4min 34s
import datetime
for api_limit, api_no in zip(range(0,200,50) ,range(9,13)):
    
    print("++++++++++++++++++++++++++++++++++++++++++++")
    API_KEY = SG_API_KEY_DICT[str(api_no)]
    print("ASTRONOMY: api_limit = ", api_limit)
    print("api_no = ", api_no)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    
    for index, row in beach_df.loc[api_limit  : api_limit + 50,].iterrows():

        print("")
        print("index = ", index)
        print("beach_name", row["beach_name"])
        print(" ")

        latitude = row['beach_latitude']
        longitude = row['beach_longitude']

        start_date = given_date
        end_date = str((datetime.datetime.strptime(given_date, "%Y-%m-%d") + datetime.timedelta(days = 1)).date())

        url_str = "https://api.stormglass.io/v2/astronomy/point?"
        url_str += "lat="+ str(latitude) +"&"
        url_str += "lng="+str(longitude) + "&"
        url_str += "start=" + start_date + "&"
        url_str += "end="+ end_date 
    #         + "&"
    #         url_str += "params=waterTemperature,wavePeriod,waveDirection,waveHeight,windWaveDirection,windWaveHeight,windWavePeriod,astronomyPeriod,secondaryastronomyPeriod,astronomyDirection,secondaryastronomyDirection,astronomyHeight,secondaryastronomyHeight,windSpeed,windDirection,airTemperature,precipitation,gust,cloudCover,humidity,pressure,visibility,currentSpeed,currentDirection,seaLevel"

        payload = {}
        headers = {
          'Authorization': API_KEY
        }
        try:
            response = requests.request("GET", url_str, headers=headers, data = payload)
            response_dict = json.loads(response.text)    
        #     print("response_dict = ", response_dict)
            astronomy_dict = {}

            for hour_dict in response_dict['data']:
        #         print("hour_dict = ", hour_dict)

                astronomy_dict['date'] = given_date

                for beach_col in beach_df.columns.tolist():
                    astronomy_dict[beach_col] = row[beach_col]     

                astronomy_col_lst = list(hour_dict.keys())
        #             astronomy_col_lst.remove("time")

                for astronomy_col in astronomy_col_lst:

                    astronomy_dict[astronomy_col] = hour_dict[astronomy_col]

        #             astronomy_dict['time'] = hour_dict['time']

                astronomy_df = astronomy_df.append(astronomy_dict, ignore_index=True)
        except:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("FAILED REQUEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("api_limit = ", api_limit)
            print("api_no = ", api_no)
            print("index = ", index)
            print("beach_name", row["beach_name"])            
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
###################################################################################################################


# # CONVERT UTC TIME TO AUSTRALIA TIME:

# In[39]:


time_col_lst = ['astronomicalDawn', 'astronomicalDusk', 'civilDawn', 'civilDusk', 'moonrise', 'moonset',
                'nauticalDawn', 'nauticalDusk', 'sunrise', 'sunset', 'time']

for time_col in time_col_lst: 
    astronomy_df[time_col] = astronomy_df[time_col].apply(lambda x: convert_datetime_in_dif_timezones(
                                                                                from_datetime_str = x, 
                                                                                from_timezone_str = 'UTC', 
                                                                                to_timezone_str ='Australia/Melbourne', 
                                                                                datetime_format = '%Y-%m-%dT%H:%M:%S+00:00'))


# In[46]:


astronomy_df.drop("moonPhase", axis=1, inplace = True)


# # CREATE astronomy_TABLE:

# In[47]:


import psycopg2 as ps

# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'test-surfers-bible-instance.cljoljhkgpfb.ap-southeast-2.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : 5432, # change to your port
               'POSTGRES_USERNAME' : 'ai_postgres', # change to your username
               'POSTGRES_PASSWORD' : 'postgres2309', # change to your password
               'POSTGRES_DBNAME' : 'test_surfers_bible_db'} # change to your db name

# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])

cur = conn.cursor()

# cur.execute("DROP TABLE SEA_WATER_QUALITY_TABLE;")

create_table_query = '''
      CREATE TABLE IF NOT EXISTS astronomy_TABLE
      (
        astronomy_id SERIAL PRIMARY KEY,
        date DATE,
        beach_id INTEGER,
        beach_name TEXT,
        beach_latitude REAL,
        beach_longitude REAL,
        beach_state TEXT,
        beach_municipality TEXT,
        astronomicalDawn TEXT,
        astronomicalDusk TEXT,
        civilDawn TEXT,
        civilDusk TEXT,
        moonFraction REAL,
        moonrise TEXT,
        moonset TEXT,
        nauticalDawn TEXT,
        nauticalDusk TEXT,
        sunrise TEXT,
        sunset TEXT,
        time TEXT,
        FOREIGN KEY (beach_id) REFERENCES beach_table(beach_id) ON DELETE CASCADE
       ); 
       '''

cur.execute(create_table_query)
conn.commit()


# # INSERT astronomy_TABLE:

# In[48]:


# %%time
# Wall time: 12min 51s
import psycopg2 as ps

# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'test-surfers-bible-instance.cljoljhkgpfb.ap-southeast-2.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : 5432, # change to your port
               'POSTGRES_USERNAME' : 'ai_postgres', # change to your username
               'POSTGRES_PASSWORD' : 'postgres2309', # change to your password
               'POSTGRES_DBNAME' : 'test_surfers_bible_db'} # change to your db name

# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])

cur = conn.cursor()

fill_question_mark_str = str(tuple(["%s"  for i in astronomy_df.columns.tolist()])).replace("'", "")
fill_question_mark_str

for row in astronomy_df.itertuples():
    data_tuple = tuple(row[1:])

    print("data_tuple = ", data_tuple)
    print(" ")
    
    cur.execute("""
                        INSERT INTO astronomy_TABLE
                        (
                            date,
                            beach_id,
                            beach_name,
                            beach_latitude,
                            beach_longitude,
                            beach_state,
                            beach_municipality,
                            astronomicalDawn,
                            astronomicalDusk,
                            civilDawn,
                            civilDusk,
                            moonFraction,
                            moonrise,
                            moonset,
                            nauticalDawn,
                            nauticalDusk,
                            sunrise,
                            sunset,
                            time
                         ) VALUES  
                         """ + fill_question_mark_str + " ;"
                , data_tuple)    

conn.commit()
cur.close()
conn.close()


# In[ ]:




