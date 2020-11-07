"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""
count = 0
password = input('Введите ваш пароль:')
for char in password:
    count += 1
    if char.isupper:
        upper_check = True
    if char.islower:
        lower_check = True
    if char.isdigit:
        digit_check = True
if count >= 8 and upper_check and lower_check and digit_check:
    print('Strong enough')
else:
    print('Too weak')

if __name__ == '__main__':
    pass
