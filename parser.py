# -*- coding: utf-8 -*-

"""
yanao_airports.parser
~~~~~~~~~~~~~~~

This module contains parsers for airports scoreboards
"""


from bs4 import BeautifulSoup
from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import requests

PATH_WEBDRIVER = 'D:\Python\yanao_airports\webdrivers\chromedriver_win32_80\chromedriver.exe'
SLY_URL = 'https://www.flightradar24.com/data/airports/sly'
SLY_ARR_URL = 'https://rasp.yandex.ru/station/9623576/?event=arrival'
SLY_DEP_URL = 'https://rasp.yandex.ru/station/9623576/?event=departure'
SLY_JSON_REQ = 'http://airshd.ru/ajax/timetable.json'
NOJ_URL = 'https://www.flightradar24.com/data/airports/noj'
NUX_URL = 'https://www.flightradar24.com/data/airports/nux'
NYM_URL = 'https://www.flightradar24.com/data/airports/nym'
SBT_URL = 'https://www.flightradar24.com/data/airports/sbt'
SBT_ARR_URL = 'http://sabetta.aero/#arrive'
SBT_DEP_URL = 'http://sabetta.aero/#sortie'

def parse_all():
    pass


def parse_sly():
    print('parse_sly')
    arr_html = get_html(SLY_ARR_URL)
    dep_html = get_html(SLY_DEP_URL)
    print(arr_html)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


def parse_noj():
    print('parse_noj')


def parse_nux():
    print('parse_nux')


def parse_nym():
    print('parse_nym')


def parse_sbt():
    print('parse_sbt')
    arr_html = get_html(SBT_ARR_URL)
    dep_html = get_html(SBT_DEP_URL)
    arr_data = sbt_get_data(arr_html, 'arrive')
    dep_data = sbt_get_data(dep_html, 'sortie')
    data = [arr_data, dep_data]
    return data


def get_html(url):
    r = requests.get(url, headers={'User-Agent': 'Custom'})
    r.encoding = r.apparent_encoding
    print(r)
    return r.text


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
    data = parse_sbt()
    print(data)