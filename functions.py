"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def even_check():
    str = input('Введите числа через пробел: ')
    number_list = list(str.split(' '))
    print(number_list)
    flag = True
    for count in (0, len(number_list)-1):
        if int(number_list[count]) % 2 == 0:
            print('Среди ваших чисел есть чётное')
            flag = False
            break
    print('Среди ваших чисел нет чётных') if flag else print()
        
    

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
sell_alcohol() if age > 21 else print('Мы не продаём алкоголь несовершеннолетним.')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()

import keyword

def keyword_check():
    word = input('Введите строку: ')
    keywords_list = dir(keyword)
    flag = False
    for count in range(0, len(keywords_list)-1):
        if word in keywords_list[count]:
            flag = True
            break
    print('Ваша строка является ключевым словом Python' if flag else 'Ваша строка не является ключевым словом Python')


keyword_check()

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type(object):
    types_dict = {'int':'Число', 'bool':'Булевый', 'str':'Строка', 'NoneType':'None', 'list':'Список', 'tuple':'Кортеж', 'set':'Множество', 'dict':'Словарь' }
    print('Вы ввели ' + types_dict[type(object).__name__])


get_type(123)