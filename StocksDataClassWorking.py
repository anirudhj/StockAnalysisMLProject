#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pandas as pd


# In[3]:



class StocksData:
    def __init__(self, api_key):
        self.api_key = api_key
      
    def get_data(self, symbol, start_date, end_date):

        BASE_URL = "https://api.polygon.io"    
       # url = f"https://api.example.com/stocks/{symbol}?api_key={self.api_key}"
        
        endpoint=f"/v2/aggs/ticker/{symbol}/range/1/day/{start_date}/{end_date}"
        params = {
                    "apiKey": self.api_key,
                    "sort": "asc",
                    "limit": 50000,
                    'Accept': 'text/csv'}
        
        response = requests.get(BASE_URL+endpoint,params)

      #  response = requests.get(url)
        if response.status_code == 200:
            data=response.json()["results"]
            Stocks = pd.DataFrame.from_dict(data, orient='columns')
            Stocks['timestamp']=pd.to_datetime(Stocks['t'],unit='ms')
            return Stocks
            
            
        else:
             return print("Error retriving the results, Code unsuccessful")

