# -*- coding: utf-8 -*-
dict_en = {}

from words_for_dict import string

#print('Входные даынне:\n' + string)

for src_string in string.split('\n'):
    on_part = src_string.split('-')
    key = on_part[0].strip(' ')
    value_src = on_part[1].strip(' ')
    for val in value_src.split(','):
        print(key)
        print(val)
        print('\n')
        #dict_en.update({key:(val.strip(' '))})

#print(dict_en)