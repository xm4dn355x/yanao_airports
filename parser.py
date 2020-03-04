# -*- coding: utf-8 -*-

"""
yanao_airports.parser
~~~~~~~~~~~~~~~

This module contains parsers for airports scoreboards
"""


from bs4 import BeautifulSoup
from time import time, strftime, gmtime
from translate_flyradar import translate
import json
import requests

TIMESTAMP = time()
SLY_URL = 'http://airshd.ru/ajax/timetable.json'
NOJ_URL = f'https://api.flightradar24.com/common/v1/airport.json?code=noj&plugin[]=&plugin-setting[schedule][mode]=&' \
          f'plugin-setting[schedule][timestamp]={TIMESTAMP}&page=1&limit=100&fleet=&token='
NUX_URL = f'https://api.flightradar24.com/common/v1/airport.json?code=nux&plugin[]=&plugin-setting[schedule][mode]=&' \
          f'plugin-setting[schedule][timestamp]={TIMESTAMP}&page=1&limit=100&fleet=&token='
NUX_ARR_URL = 'http://nux.aero/board/?type=arr&ready=yes'
NUX_DEP_URL = 'http://nux.aero/board/?ready=yes'
NYM_URL = f'https://api.flightradar24.com/common/v1/airport.json?code=nym&plugin[]=&plugin-setting[schedule][mode]=&' \
          f'plugin-setting[schedule][timestamp]={TIMESTAMP}&page=1&limit=100&fleet=&token='
SBT_ARR_URL = 'http://sabetta.aero/#arrive'
SBT_DEP_URL = 'http://sabetta.aero/#sortie'


def parse_all():
    return [parse_sly(), parse_noj(), parse_nux(), parse_nym(), parse_sbt()]


def get_html(url):
    """
    Get HTML document from GET request from URL

    :param url: str URL of request
    :return: str HTML document
    """
    r = requests.get(url, headers={'User-Agent': 'Custom'})
    r.encoding = r.apparent_encoding
    print(r)
    return r.text


def get_json(url):
    """
    Get JSON document from GET request from URL

    :param url:
    :return: dict JSON data
    """
    global TIMESTAMP
    TIMESTAMP = time()
    r = requests.get(url, headers={'User-Agent': 'Custom'})
    json_data = json.loads(r.text)
    return json_data


def parse_sly():
    """
    Parsing Salekhard (SLY) airport arrivals and departure data

    :return: list [list of dicts arrivals, list of dicts departures]
    """
    print('parse_sly')
    json_data = get_json(SLY_URL)
    data = json_data.get('data')
    arr_data = get_sly_parsed_data(data, 'ARRIVAL')
    dep_data = get_sly_parsed_data(data, 'DEPARTURE')
    data = [arr_data, dep_data]
    return data


def get_sly_parsed_data(raw_data, type):
    """
    Recieve raw JSON data and return list of dicts with flights data

    :param raw_data: dict JSON data
    :param type: str 'ARRIVAL' or 'DEPARTURE'
    :return: list of dicts with parsed data
    """
    rows = raw_data.get(type)
    data = []
    for row in rows:
        row_data = {'flight': row['flight'], 'airport': row['airport'], 'plane': row['aircraft'],
                    'plan_time': row['plan'], 'fact_time': row['fact'], 'status': row['status'].upper()}
        data.append(row_data)
    return data


def parse_noj():
    """
    Parsing Nojabrsk (NOJ) airport arrivals and departure data

    :return: list [list of dicts arrivals, list of dicts departures]
    """
    print('parse_noj')
    json_data = get_json(NOJ_URL).get('result').get('response').get('airport').get('pluginData').get('schedule')
    arr_data = get_flyradar_json_data(json_data, 'arrivals')
    dep_data = get_flyradar_json_data(json_data, 'departures')
    data = [arr_data, dep_data]
    return data


def parse_nux():
    """
    Parsing Noviy Urengoy (NUX) airport arrivals and departure data

    :return: list [list of dicts arrivals, list of dicts departures]
    """
    print('parse_nux')
    arr_html = get_html(NUX_ARR_URL)
    dep_html = get_html(NUX_DEP_URL)
    arr_data = nux_get_data(arr_html)
    dep_data = nux_get_data(dep_html)
    data = [arr_data, dep_data]
    return data


def nux_get_data(html):
    """
    Recieve HTML document and return parsed data from this HTML

    :param html: str HTML document
    :return: list of dicts with parsed data
    """
    soup = BeautifulSoup(html, 'lxml')
    rows = soup.find('div', 'table-flex-wrap').find('div', 'table-flex__body').find_all('a')
    data = []
    for row in rows:
        flight = row.find('div', 'table-flex__td table-flex__td--type2').find('span').text
        airport = row.find('div', 'table-flex__td table-flex__td--type4').find('span', 'board__text').text
        try:
            plane = row.find('div', 'table-flex__td table-flex__td--type3').find('div', 'table-aircompany-logo-alt')\
                .text
        except :
            plane = ''
        plan_time = f"{row.find('div', 'table-flex__td table-flex__td--type1').find('span', 'board__text').text} " \
                    f"{row.find('div', 'table-flex__td table-flex__td--type1').find('span', 'board__text-extra').text}"
        fact_time = f"{row.find('div', 'table-flex__td table-flex__td--type6').find('span', 'board__text').text} " \
                    f"{row.find('div', 'table-flex__td table-flex__td--type6').find('span', 'board__text-extra').text}"
        status = row.find('div', 'table-flex__td table-flex__td--type5').find('span').text.upper()
        row_data = {'flight': flight, 'airport': airport, 'plane': plane, 'plan_time': plan_time,
                    'fact_time': fact_time, 'status': status}
        data.append(row_data)
    return data



def parse_nym():
    """
    Parsing Nadym (NYM) airport arrivals and departure data

    :return: list [list of dicts arrivals, list of dicts departures]
    """
    print('parse_nym')
    json_data = get_json(NYM_URL).get('result').get('response').get('airport').get('pluginData').get('schedule')
    arr_data = get_flyradar_json_data(json_data, 'arrivals')
    dep_data = get_flyradar_json_data(json_data, 'departures')
    data = [arr_data, dep_data]
    return data


def get_flyradar_json_data(json_data, type):
    """
    Recieve JSON from flightradar24 'arrivals' or 'departure', parsing JSON and return list of dicts with parsed data

    :param json_data: dict JSON
    :param type: str 'arrivals' or 'departures'
    :return: list of dicts with parsed data
    """
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
        plan_time = convert_timestamp_to_strftime(row.get('time').get('scheduled').get(time_type))
        try:
            fact_time = convert_timestamp_to_strftime(row.get('time').get('estimated').get(time_type))
        except:
            fact_time = ''
        status = translate(row.get('status').get('text'), 'status')
        row_data = {'flight': flight, 'airport': airport, 'plane': plane,
                    'plan_time': plan_time, 'fact_time': fact_time, 'status': status}
        data.append(row_data)
    return data


def parse_sbt():
    """
    Parsing Sabetta (SBT) airport arrivals and departure data

    :return: list [list of dicts arrivals, list of dicts departures]
    """
    print('parse_sbt')
    arr_html = get_html(SBT_ARR_URL)
    dep_html = get_html(SBT_DEP_URL)
    arr_data = sbt_get_data(arr_html, 'arrive')
    dep_data = sbt_get_data(dep_html, 'sortie')
    data = [arr_data, dep_data]
    return data


def sbt_get_data(html, type):
    """
    Recieve HTML document and str 'arrive' or 'sortie', parse HTML and return list of dicts with parsed data

    :param html: str HTML document
    :param type: str 'arrive' or 'sortie'
    :return:
    """
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
        status = tds[5].find('span').text.strip().upper()
        row_data = {'flight': flight, 'airport': airport, 'plane': plane, 'plan_time': plan_time,
                    'fact_time': fact_time, 'status': status}
        data.append(row_data)
    return data


def convert_timestamp_to_strftime(time_var):
    """
    Revieve timestamp and return str with Humanized time data
    :param time_var: int timestamp
    :return: str "Hours:Minutes day.month"
    """
    return strftime("%H:%M %d.%m", gmtime(time_var))


if __name__ == '__main__':
    print('parser')
    data = parse_all()
    print('SLY')
    print('arrivals')
    for row in data[0][0]:
        print(row)
    print('departure')
    for row in data[0][1]:
        print(row)
    print()

    print('NOJ')
    print('arrivals')
    for row in data[1][0]:
        print(row)
    print('departure')
    for row in data[1][1]:
        print(row)
    print()

    print('NUX')
    print('arrivals')
    for row in data[2][0]:
        print(row)
    print('departure')
    for row in data[2][1]:
        print(row)
    print()

    print('NYM')
    print('arrivals')
    for row in data[3][0]:
        print(row)
    print('departure')
    for row in data[3][1]:
        print(row)
    print()

    print('SBT')
    print('arrivals')
    for row in data[4][0]:
        print(row)
    print('departure')
    for row in data[4][1]:
        print(row)
    print()