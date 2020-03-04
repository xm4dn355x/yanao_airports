# -*- coding: utf-8 -*-

"""
yanao_airports.translate_flyradar
~~~~~~~~~~~~~~~

This module contains func for translate flightradar24 parsed data to Russian language
"""

import re


def translate(str, type):
    res = str
    if type == 'status':
        if re.findall('Scheduled', str):
            res = str.replace('Scheduled', 'ПО РАСПИСАНИЮ')
        if re.findall('Estimated', str):
            res = str.replace('Estimated', 'ОЖИДАЕТСЯ')
        if re.findall('Canceled', str):
            res = str.replace('Canceled', 'ОТМЕНЕН')
    return res