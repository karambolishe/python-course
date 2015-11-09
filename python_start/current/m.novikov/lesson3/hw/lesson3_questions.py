# -*- encoding: utf-8 -*-
source_file = open('words')

get_list = [i.rstrip() for i in source_file]

# Задание 1: Вывести самое длинное слово
longest = max(get_list, key=len)
print('Task #1\nLongest word: %s;\nhis lenght: %s' % (longest, len(longest)))

# Задание 2: Вывести все слова, где есть буква 's' встречается больше 5 раз
words_with_s = []
dict_for_two_task = {}
for string in get_list:
    get_list_word = list(string)
    if get_list_word.count('s') > 5:
        words_with_s.append(string)

    for letter in get_list_word:
        if letter in dict_for_two_task:
            dict_for_two_task[letter] += 1
        else:
            dict_for_two_task.setdefault(letter, 0)
            dict_for_two_task[letter] += 1

print('\nTask #2\nWord with ss:')
for word in words_with_s:
    print('\t%s' % (word))

# Задание 3: Вывести самую частую букву (делать через dict)
only_value = dict_for_two_task.values()
only_value.sort()
popular_val = int(only_value[-1])
global popular_key
for key in dict_for_two_task.keys():
    val = dict_for_two_task[key]
    if val == popular_val:
        popular_key = key

print('\nTask #3\nPopular letter is: %s \nCount: %s' % (popular_key, popular_val))

# Задание 4: Вывести все слова, состоящие из тех же букв, что и слово 'international' (делать через set)
inter_set = set('international')
finded = [w for w in get_list if set(w) == inter_set]

print('\nTask #4\nFrom this words we can get international:')
for word in finded:
    print('\t%s' % (word))