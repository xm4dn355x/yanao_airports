"""
airports data updater module

created by https://github.com/xm4dn355x
"""


from airports_parser import parse_all
from configs import POSTGRES_CONF

def update_db():
    print('update_db')
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


def delete_old_data(old_data):
    print('delete_old_data')


def insert_to_table(table_name, data):
    print('insert_to_table')


def select_all_from_talbe(table_name):
    print('select_all_from_table')


if __name__ == '__main__':
    update_db()
