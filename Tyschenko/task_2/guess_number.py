# -*- coding: utf-8 -*-

def print_quest(cond, val_q):
    return raw_input('Ваше число, {0} {1}?(y/n): '.format(cond, val_q))

def print_answer(val_a):
     print('Ваше число - {0} '.format(val_a))


x = int(raw_input('Загадайте число от 1 до 5:'))

answer_more3 = print_quest('больше', '3')
if answer_more3 == 'y':
    answer4 = print_quest('это', '4')
    if answer4 == 'y':
        print_answer('4')
    else:
        print_answer('5')
else:
    answer_less3 = print_quest('меньше', '3')
    if answer_less3 == 'y':
        answer1 = print_quest('это', '1')
        if answer1 == 'y':
            print_answer('1')
        else:
            print_answer('2')
    else:
        print_answer('3')