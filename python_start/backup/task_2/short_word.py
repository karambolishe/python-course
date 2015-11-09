# -*- coding: utf-8 -*-

short_word = ''
transf_string = ''
correct_input = 1
src_string = ''


while correct_input == 1:
    src_string = raw_input('Введите строку: ')
    if src_string == '':
        print('Enter correct string please')
    else:
        correct_input = 0

lenght_string = len(src_string)

for letter in src_string:
    if str.isalpha(letter):
        transf_string += letter
    else:
        if transf_string[-1] != '*':
            transf_string += '*'

if transf_string[-1] == '*':
    transf_string = transf_string[:-1]

if '*' not in transf_string:
    short_word = transf_string
    print(transf_string)
else:
    transf_string = transf_string.split('*')

    for word in transf_string:
        if len(word) < lenght_string:
            lenght_string = len(word)
            short_word = word

print('It is short word: {0} and it have lenght: \
{1}'.format(str.upper(short_word), len(short_word)))