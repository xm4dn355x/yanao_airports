"""
airports data updater module

created by https://github.com/xm4dn355x
"""


import psycopg2
import threading
from airports_parser import parse_all
from configs import PG_CONF
from psycopg2.extras import DictCursor
from psycopg2.extensions import AsIs
from time import time


FLIGHTS = 'dashboard_flights'


def db_update_loop():
    start_time = time()
    print('Парсинг аэропортов ЯНАО.')
    try:
        update_db()
    except :
        print('Ошибка во время выполнения парсинга')
    print(f"""Время выполнения: {round((time() - start_time), 2) }""")
    threading.Timer(300, db_update_loop).start()


def update_db():
    print('Updating airports status')
    old_data = select_all_from_talbe(FLIGHTS)
    try:
        data = parse_all()
        for row in data[0][0]:
            prepared_data = prepare_data('Салехард', 'ПРИЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[0][1]:
            prepared_data = prepare_data('Салехард', 'ВЫЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[1][0]:
            prepared_data = prepare_data('Ноябрьск', 'ПРИЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[1][1]:
            prepared_data = prepare_data('Ноябрьск', 'ВЫЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[2][0]:
            prepared_data = prepare_data('Новый Уренгой', 'ПРИЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[2][1]:
            prepared_data = prepare_data('Новый Уренгой', 'ВЫЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[3][0]:
            prepared_data = prepare_data('Надым', 'ПРИЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[3][1]:
            prepared_data = prepare_data('Надым', 'ВЫЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[4][0]:
            prepared_data = prepare_data('Сабетта', 'ПРИЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        for row in data[4][1]:
            prepared_data = prepare_data('Сабетта', 'ВЫЛЕТ', row)
            insert_to_table(FLIGHTS, prepared_data)
        delete_from_table(FLIGHTS, old_data)
        print('flights data updated')
    except :
        print('parsing failure')


def prepare_data(airport, flight_type, data):
    res = {
        'orig_airport': airport,
        'flight_type': flight_type,
        'flight': data['flight'],
        'dest_airport': data['airport'],
        'plane': data['plane'],
        'plan_time': data['plan_time'],
        'fact_time': data['fact_time'],
        'status': data['status'],
    }
    return res


def delete_from_table(table_name, data):
    conn = psycopg2.connect(dbname=PG_CONF['NAME'], user=PG_CONF['USER'], password=PG_CONF['PWD'], host=PG_CONF['HOST'])
    cursor = conn.cursor(cursor_factory=DictCursor)
    for d in data:
        delete_statement = f"DELETE FROM {table_name} WHERE id='{d['id']}'"
        cursor.execute(delete_statement)
    conn.commit()
    conn.close()


def insert_to_table(table_name, data):
    conn = psycopg2.connect(dbname=PG_CONF['NAME'], user=PG_CONF['USER'], password=PG_CONF['PWD'], host=PG_CONF['HOST'])
    cursor = conn.cursor(cursor_factory=DictCursor)
    columns = data.keys()
    values = [data[column] for column in columns]
    insert_statement = f'INSERT INTO {table_name} (%s) VALUES %s'
    cursor.execute(insert_statement, (AsIs(','.join(columns)), tuple(values)))
    conn.commit()
    conn.close()


def select_all_from_talbe(table_name):
    print('select_all_from_table')
    conn = psycopg2.connect(dbname=PG_CONF['NAME'], user=PG_CONF['USER'], password=PG_CONF['PWD'], host=PG_CONF['HOST'])
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute(f'SELECT * FROM {table_name}')
    res = cursor.fetchall()
    conn.close()
    return res


if __name__ == '__main__':
    db_update_loop()
