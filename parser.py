# -*- coding: utf-8 -*-

"""
yanao_airports.parser
~~~~~~~~~~~~~~~

This module contains parsers for airports scoreboards
"""


from bs4 import BeautifulSoup
from datetime import datetime
import json
import requests


SLY_URL = 'http://airshd.ru/ajax/timetable.json'
NOJ_URL = 'https://api.flightradar24.com/common/v1/airport.json?code=noj&plugin[]=&plugin-setting[schedule][mode]=&' \
          'plugin-setting[schedule][timestamp]=1583128067&page=1&limit=100&fleet=&token='
NUX_URL = 'https://api.flightradar24.com/common/v1/airport.json?code=nux&plugin[]=&plugin-setting[schedule][mode]=&' \
          'plugin-setting[schedule][timestamp]=1583141149&page=1&limit=100&fleet=&token='
NYM_URL = 'https://api.flightradar24.com/common/v1/airport.json?code=nym&plugin[]=&plugin-setting[schedule][mode]=&' \
          'plugin-setting[schedule][timestamp]=1583141149&page=1&limit=100&fleet=&token='
SBT_ARR_URL = 'http://sabetta.aero/#arrive'
SBT_DEP_URL = 'http://sabetta.aero/#sortie'


def parse_all():
    sly_data = parse_sly()
    noy_data = parse_noj()
    nux_data = parse_nux()
    nym_data = parse_nym()
    sbt_data = parse_sbt()
    parsed_data = [sly_data, noy_data, nux_data, nym_data, sbt_data]
    return parsed_data


def get_html(url):
    r = requests.get(url, headers={'User-Agent': 'Custom'})
    r.encoding = r.apparent_encoding
    print(r)
    return r.text


def get_json(url):
    r = requests.get(url, headers={'User-Agent': 'Custom'})
    json_data = json.loads(r.text)
    return json_data


def parse_sly():
    print('parse_sly')
    json_data = get_json(SLY_URL)
    data = json_data.get('data')
    arr_data = get_sly_parsed_data(data, 'ARRIVAL')
    dep_data = get_sly_parsed_data(data, 'DEPARTURE')
    data = [arr_data, dep_data]
    return data


def get_sly_parsed_data(raw_data, type):
    rows = raw_data.get(type)
    data = []
    for row in rows:
        row_data = {'flight': row['flight'], 'airport': row['airport'], 'plane': row['aircraft'],
                    'plan_time': row['plan'], 'fact_time': row['fact'], 'status': row['status']}
        data.append(row_data)
    return data


def parse_noj():
    print('parse_noj')
    json_data = get_json(NOJ_URL).get('result').get('response').get('airport').get('pluginData').get('schedule')
    arr_data = get_flyradar_json_data(json_data, 'arrivals')
    dep_data = get_flyradar_json_data(json_data, 'departures')
    data = [arr_data, dep_data]
    return data


def parse_nux():
    print('parse_nux')
    json_data = get_json(NUX_URL).get('result').get('response').get('airport').get('pluginData').get('schedule')
    arr_data = get_flyradar_json_data(json_data, 'arrivals')
    dep_data = get_flyradar_json_data(json_data, 'departures')
    data = [arr_data, dep_data]
    return data


def parse_nym():
    print('parse_nym')
    json_data = get_json(NYM_URL).get('result').get('response').get('airport').get('pluginData').get('schedule')
    arr_data = get_flyradar_json_data(json_data, 'arrivals')
    dep_data = get_flyradar_json_data(json_data, 'departures')
    data = [arr_data, dep_data]
    return data


def get_flyradar_json_data(json_data, type):
    rows = json_data.get(type).get('data')
    if type == 'arrivals':
        airport_type = 'origin'
        time_type = 'arrival'
    elif type == 'departures':
        airport_type = 'destination'
        time_type = 'departure'
    else:
        return None
    data = []
    for row in rows:
        row = row.get('flight')
        flight = row.get('identification').get('number').get('default')
        airport = row.get('airport').get(airport_type).get('name')
        plane = row.get('aircraft').get('model').get('code')
        plan_time = datetime.fromtimestamp(row.get('time').get('scheduled').get(time_type))
        try:
            fact_time = datetime.fromtimestamp(row.get('time').get('estimated').get(time_type))
        except:
            fact_time = ''
        status = row.get('status').get('text')
        row_data = {'flight': flight, 'airport': airport, 'plane': plane,
                    'plan_time': plan_time, 'fact_time': fact_time, 'status': status}
        data.append(row_data)
    return data


def parse_sbt():
    print('parse_sbt')
    arr_html = get_html(SBT_ARR_URL)
    dep_html = get_html(SBT_DEP_URL)
    arr_data = sbt_get_data(arr_html, 'arrive')
    dep_data = sbt_get_data(dep_html, 'sortie')
    data = [arr_data, dep_data]
    return data


def sbt_get_data(html, type):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', id=type)
    table = table.find('tbody')
    rows = table.find_all('tr')
    data = []
    for row in rows:
        tds = row.find_all('td')
        flight = tds[0].find('a').text
        airport = tds[1].text.strip()
        plane = tds[2].text.strip()
        plan_time = tds[3].text.strip()
        fact_time = tds[4].text.strip()
        status = tds[5].find('span').text.strip()
        row_data = {'flight': flight, 'airport': airport, 'plane': plane, 'plan_time': plan_time,
                    'fact_time': fact_time, 'status': status}
        data.append(row_data)
    return data


if __name__ == '__main__':
    print('parser')