import requests
import json
from datetime import datetime, timedelta
# Module for pulling market data from FRED

#set dates based on today's date

def today_value():

    def buffer(x):
        x = x - timedelta(days=7)
        return x

    today_end_date = datetime.today()
    today_start_date = buffer(today_end_date)

    last_month_end_date = datetime.today().replace(day=1)
    last_month_end_date = last_month_end_date - timedelta(days=1)
    last_month_start_date = buffer(last_month_end_date)


    payload = {
        "series_id" : "DGS10",
        "api_key" : "fe2f1e3d86308243b33bd5adc4174e6a",
        "file_type" : "json",
        "frequency" : "d",
        "observation_start" : today_start_date.strftime('%Y-%m-%d'),
        "observation_end" : today_end_date.strftime('%Y-%m-%d'),
        "sort_order" : "desc"
    }

    r = requests.get('https://api.stlouisfed.org/fred/series/observations', params=payload)
    r = r.json()
    #print("ten year yield as of " + today_start_date.strftime('%Y-%m-%d'))
    #print(r["observations"][0]["value"])

    today_value = r["observations"][0]["value"]
    return today_value

#payload = {
#    "series_id" : "DGS10",
#    "api_key" : "fe2f1e3d86308243b33bd5adc4174e6a",
#    "file_type" : "json",
#    "frequency" : "d",
#    "observation_start" : last_month_start_date.strftime('%Y-%m-%d'),
#    "observation_end" : last_month_end_date.strftime('%Y-%m-%d'),
#    "sort_order" : "desc"
#}


print(today_value())
#r = requests.get('https://api.stlouisfed.org/fred/series/observations', params=payload)
#r = r.json()

#print("ten year yield as of " + last_month_end_date.strftime('%Y-%m-%d'))
#print(r["observations"][0]["value"])
