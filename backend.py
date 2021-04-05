from hijri_converter import convert
from datetime import timedelta, date
from function import binary_search
import sys


class my_dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

correct_list = []
list_key = []
list_val = []
dict_search_result = my_dictionary

def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def getstrftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


start_dt = date(2020, 12, 29)
end_dt = date(2020, 12, 31)

for dt in daterange(start_dt, end_dt):
    y = int(dt.strftime("%Y"))
    m = int(dt.strftime("%m"))
    d = int(dt.strftime("%d"))
    hijri = convert.Gregorian(y, m, d).to_hijri()
    hdt = hijri.datetuple()
    list_key.append(getstrftime('%A, %B {S}, %Y', dt))
    list_val.append(f"{hijri.day_name()}, {hijri.month_name()} {(hdt[2])}{suffix(hdt[2])}, {hdt[0]}")
print(list_key)
print('')
for e in list_key:
    # print(e.split())
    split_e = e.split()
    search_e = binary_search(split_e, 'December')
    if search_e == -1:
         sys.exit(f'Error: {search_e}')
    else:
        correct_list.append(e)
    for f in correct_list:
        print(f)
        amount_in_list = len(f)
        dict_search_result.add()
# x = str(input('Date: '))
#
# search = (binary_search(list_key, x))
# if search == -1:
#     print(f'Error: {search}')
#     sys.exit(f'{x} is not found')
# else:
#     print(list_val[search])
#
