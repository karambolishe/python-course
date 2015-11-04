# -*- coding: utf-8 -*-
d_en_lat = {}
d_lat_en = {}

from words_for_dict import string

def printing(dict):
    for key in sorted(dict):
        print key.ljust(8) + ' - ' + ', '.join(dict[key])

for src_string in string.split('\n'):
    devided_on_part = src_string.split('-')
    key = devided_on_part[0].strip(' ')
    value_src = devided_on_part[1].strip(' ')
    value_lat = [i.strip(' ') for i in str.split(value_src, ',')]

    d_en_lat[key] = value_lat

for key in d_en_lat:
    value_en_list = d_en_lat[key]
    for value_en in value_en_list:
        if value_en not in d_lat_en:
            d_lat_en[value_en] = [key]
        else:
            d_lat_en[value_en].append(key)

#printing(d_lat_en)

print 'Входные даынне:\n' + str(len(d_en_lat))
printing(d_en_lat)
print 'Выходные даынне:\n' + str(len(d_lat_en))
printing(d_lat_en)