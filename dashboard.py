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

    today_value = r["observations"][0]["value"]
    today_date = r["observations"][0]["date"]
    return today_value, today_date



def last_month_value(series):

    def buffer(x):
        x = x - timedelta(days=5)
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
    last_month_date = r["observations"][0]["date"]
    return last_month_value, last_month_date

def last_quarter_value(series):

    #today = datetime.today()
    #if today.month == 10 or 11 or 12:
    #    today = today.replace(month=9,day=30)
    #elif today.month == 7 or 8 or 9:
    #    today = today.replace(month=6,day=30)
    #elif today.month == 4 or 5 or 6:
    #    today = today.replace(month=3,day=31)
    #elif today.month == 1 or 2 or 3:
    #    today = datetime.today() - timedelta(days=365)
    #    today = today.replace(day=31, month =12)

    def buffer(x):
        x = x - timedelta(days=7)
        return x

    today = datetime.today()
    if today.month in (1,2,3):
        last_quarter_end_date = datetime.today() - timedelta(days=365)
        last_quarter_end_date = last_quarter_end_date.replace(day=31,month=12)
        last_quarter_start_date = buffer(last_quarter_end_date)
    if today.month in (10,11,12):
        today = today.replace(month=9,day=30)
        last_quarter_end_date = today
        last_quarter_start_date = buffer(last_quarter_end_date)
    if today.month in (7,8,9):
        today = today.replace(month=6,day=30)
        last_quarter_end_date = today
        last_quarter_start_date = buffer(last_quarter_end_date)
    if today.month in (4,5,6):
        today = today.replace(month=3,day=31)
        last_quarter_end_date = today
        last_quarter_start_date = buffer(last_quarter_end_date)

    payload = {
        "series_id" : series,
        "api_key" : "fe2f1e3d86308243b33bd5adc4174e6a",
        "file_type" : "json",
        "frequency" : "d",
        "observation_start" : last_quarter_start_date.strftime('%Y-%m-%d'),
        "observation_end" : last_quarter_end_date.strftime('%Y-%m-%d'),
        "sort_order" : "desc"
    }

    r = requests.get('https://api.stlouisfed.org/fred/series/observations', params=payload)
    r = r.json()
    last_quarter_value = r["observations"][0]["value"]
    last_quarter_date = r["observations"][0]["date"]

    return last_quarter_value, last_quarter_date


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
    last_year_date = r["observations"][0]["date"]
    return last_year_value, last_year_date


def get_series():
    series = ["DGS1","DGS2","DGS5","DGS10","DGS30","BAMLH0A0HYM2","BAMLC0A0CM","BAMLC0A4CBBB","BAMLC0A3CA","BAMLC0A2CAA","BAMLC0A1CAAA"]
    series_names = {
    "DGS1" : "1Y US Treasury",
    "DGS2" : "2Y US Treasury",
    "DGS5" : "5Y US Treasury",
    "DGS10" : "10Y US Treasury",
    "DGS30" : "30Y US Treasury",
    "BAMLH0A0HYM2" : "US High Yield OAS",
    "BAMLC0A0CM" : "US IG Corporate OAS",
    "BAMLC0A4CBBB" : "BBB Corp OAS",
    "BAMLC0A3CA" : "A Corp OAS",
    "BAMLC0A2CAA" : "AA Corp OAS",
    "BAMLC0A1CAAA": "AAA Corp OAS",

    }
    return series, series_names

def collect_values():
    series, series_names = get_series()
    values = [[],[],[],[],[],[],[]]

    for x in series:
        todays_values, todays_date = today_value(x)
        values[0].append(todays_values)
        last_months_values, last_month_date = last_month_value(x)
        values[1].append(last_months_values)
        last_quarters_value, last_quarters_date = last_quarter_value(x)
        values[2].append(last_quarters_value)
        last_years_values, last_years_date = last_year_value(x)
        values[3].append(last_years_values)
        values[4].append(series_names[x])
        values[5] = [todays_date, last_month_date, last_quarters_date, last_years_date]
        values[6].append(str(round(100*((float(todays_values)-float(last_years_values))),0)))
    return values
