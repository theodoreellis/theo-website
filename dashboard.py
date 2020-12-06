import requests
import json
from datetime import datetime, timedelta
# Module for pulling market data from FRED

#set dates based on today's date




def today_value(series):

    def buffer(x):
        x = x - timedelta(days=7)
        return x

    today_end_date = datetime.today()
    today_start_date = buffer(today_end_date)

    last_month_end_date = datetime.today().replace(day=1)
    last_month_end_date = last_month_end_date - timedelta(days=1)
    last_month_start_date = buffer(last_month_end_date)


    payload = {
        "series_id" : series,
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



def last_month_value(series):

    def buffer(x):
        x = x - timedelta(days=7)
        return x

    last_month_end_date = datetime.today().replace(day=1)
    last_month_end_date = last_month_end_date - timedelta(days=1)
    last_month_start_date = buffer(last_month_end_date)


    payload = {
        "series_id" : series,
        "api_key" : "fe2f1e3d86308243b33bd5adc4174e6a",
        "file_type" : "json",
        "frequency" : "d",
        "observation_start" : last_month_start_date.strftime('%Y-%m-%d'),
        "observation_end" : last_month_end_date.strftime('%Y-%m-%d'),
        "sort_order" : "desc"
    }

    r = requests.get('https://api.stlouisfed.org/fred/series/observations', params=payload)
    r = r.json()
    #print("ten year yield as of " + today_start_date.strftime('%Y-%m-%d'))
    #print(r["observations"][0]["value"])

    last_month_value = r["observations"][0]["value"]
    return last_month_value


def last_year_value(series):

    def buffer(x):
        x = x - timedelta(days=7)
        return x

    last_year_end_date = datetime.today() - timedelta(days=365)
    last_year_end_date = last_year_end_date.replace(day=31, month=12)
    last_year_start_date = buffer(last_year_end_date)

    payload = {
        "series_id" : series,
        "api_key" : "fe2f1e3d86308243b33bd5adc4174e6a",
        "file_type" : "json",
        "frequency" : "d",
        "observation_start" : last_year_start_date.strftime('%Y-%m-%d'),
        "observation_end" : last_year_end_date.strftime('%Y-%m-%d'),
        "sort_order" : "desc"
    }

    r = requests.get('https://api.stlouisfed.org/fred/series/observations', params=payload)
    r = r.json()
    #print("ten year yield as of " + today_start_date.strftime('%Y-%m-%d'))
    #print(r["observations"][0]["value"])

    last_year_value = r["observations"][0]["value"]
    return last_year_value


def get_series():
    series = ["DGS1","DGS2","DGS5","DGS10"]
    series_names = {
    "DGS1" : "1Y US Treasury",
    "DGS2" : "2Y US Treasury",
    "DGS5" : "5Y US Treasury",
    "DGS10" : "10Y US Treasury"
    }
    return series, series_names

def collect_values():
    series, series_names = get_series()
    values = [[],[],[],[]]
    #for i in range(0,len(series)):
    #    values.append([])
    for x in series:
        todays_values = today_value(x)
        values[0].append(todays_values)
        last_months_values = last_month_value(x)
        values[1].append(last_months_values)
        last_years_values = last_year_value(x)
        values[2].append(last_years_values)
        values[3].append(series_names[x])
    return values
