# -*- coding: utf-8 -*-

"""
yanao_airports.translate_flyradar
~~~~~~~~~~~~~~~

This module contains func for translate flightradar24 parsed data to Russian language
"""

import re


def translate(str, type):
    """
    Recieve english text and type of field, translate it into russian and return this string

    :param str: str
    :param type: str  type of field Like: 'status'
    :return: str translated text
    """
    res = str
    if type == 'status':
        if re.findall('Scheduled', str):
            res = str.replace('Scheduled', 'ПО РАСПИСАНИЮ')
        if re.findall('Estimated', str):
            res = str.replace('Estimated', 'ОЖИДАЕТСЯ')
        if re.findall('Canceled', str):
            res = str.replace('Canceled', 'ОТМЕНЕН')
    return res