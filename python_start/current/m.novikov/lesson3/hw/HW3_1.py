# -*- encoding: utf-8 -*-
'''
Task 1
Создать список положительных и отрицательных вещественных чисел.
Получить из этого списка другой список, состоящий только из положительных
элементов первого, стоящих на четных местах.
'''

import random

try:
    wich_you_get_num = input('How many elements do you wish in array?: ')
except ValueError:
    print('Please enter int type!')


global list_num
global list_positive
global list_negative
list_num = []
list_negative = []
list_positive = []

def create_list(wich_count_dig):
    for count_num in range(wich_count_dig):
        list_num.append(random.uniform(-50.0, 50.0))

create_list(20)

for get_val in list_num:
    if get_val >= 0:
        list_positive.append(get_val)
    if get_val < 0:
        list_negative.append(get_val)

print('Negative list: %s\nPositive list: %s ' % (list_negative, list_positive))

'''
Task 2
В списке чисел проверить, все ли элементы являются уникальными,
т.е. каждое число встречается только один раз.
'''
try:
    wich_you_get_try = int(input('How many try do you want?: '))
except ValueError:
    print('Please enter int type!')

try:
    wich_you_get_range = int(input('How do you want range of digits?: '))
except ValueError:
    print('Please enter int type!')

list_num.clear()
for val in range(wich_you_get_try):
    list_num.append(random.randrange(0, wich_you_get_range))

length_list = len(list_num)
length_set = len(set(list_num))
if length_list == length_set:
    print('Values in list is unique', list_num)
else:
    print('Values in list is not unique', list_num)