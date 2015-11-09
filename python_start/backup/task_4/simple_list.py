# -*- coding: utf-8 -*-
__author__ = 'nikolay'

L_tru_condit= []
L_filtered = []
L = [80, 35, 30, 98, 35, 4, 94, 51, 22, 22, 52, 97, 67, 90, 9, 1, 87, 78, 100, 29]

for val in L:
    if 35 < val < 65:
        L_tru_condit.append(val)
    else:
        L_filtered.append(val)

print('A = {0} - список с начальными элементами'.format(L))
print('B = {0} - отфильтрованный список'.format(L_filtered))
print('C = {0} - список с удаленными элементами'.format(L_tru_condit))
