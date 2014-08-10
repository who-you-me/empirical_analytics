# -*- coding: utf-8 -*-

import csv
from xlrd import open_workbook


def is_municipality_row(row):
    city_code = row[0].strip()
    return city_code.isdigit() and len(city_code) == 5

def is_designed_city(city_code):
    designed_city = (
        '01100', '04100', '11100', '12100', '14100',
        '14130', '14150', '15100', '22100', '22130',
        '23100', '26100', '27100', '27140', '28100',
        '33100', '34100', '40100', '40130'
    )
    return city_code in designed_city

def is_tokyo_ward(city_code):
    return city_code.startswith('131') and city_code[-2:] != '00'

def is_acceptalbe_municipality(city_code):
    if city_code[2:] >= '201':
        return True
    elif is_designed_city(city_code):
        return True
    elif is_tokyo_ward(city_code):
        return True
    else:
        return False

def get_city(row):
    return (row[0].strip(), row[1].strip())

def get_value(sheet, index):
    for number in range(0, sheet.nrows):
        row = sheet.row_values(number)
        if is_municipality_row(row):
            city_code, city_name = get_city(row)
            if is_acceptalbe_municipality(city_code):
                yield [city_code, city_name, int(row[index])]


if __name__ == '__main__':
    names = (('pop', 2), ('unemp', 4), ('crime', 4))
    result = {}
    for name in names:
        book = open_workbook(name[0] + '.xls')
        sheet = book.sheet_by_index(0)

        for city_code, city_name, value in get_value(sheet, name[1]):
            result.setdefault(city_code, {})
            result[city_code]['name'] = city_name
            result[city_code][name[0]] = value

    with open('crime.csv', 'w') as f:
        writer = csv.writer(f)
        colnames = ['id', 'crime', 'unemp', 'pop']
        writer.writerow(colnames)
        for key, value in sorted(result.items()):
            row = [key] + [value[col] for col in colnames[1:]]
            writer.writerow(row)
