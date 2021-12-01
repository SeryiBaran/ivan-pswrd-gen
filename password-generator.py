# Генератор паролей
# Меньше 12 символов пароль слабый, ставьте больше

# Набор символов с похожими друг на друга(i,I,1,l,L):
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

# Набор символов без похожих друг на друга букв (по умолчанию):
# abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789

import random

default_type = '1'
default_col = 12
simbols_no_repeat = list('abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789')
simbols_repeat = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

def input_type():
    type_pswrd_loc = input('\n\nКакой набор символов использовать,\nс похожими символами (i, L, l, 1) или без похожих?\n(без похожих - 1)\n(с похожими - 2)\n(Можете оставить по умолчанию, нажав ENTER)\n: ')
    return type_pswrd_loc
def input_col():
    col_pswrd_loc = input('\n\nКакой длины пароль сгенерировать?\n(Меньше 12 не рекомендую, можете оставить по умолчанию, нажав ENTER)\n: ')
    return col_pswrd_loc



type_pswrd = input_type()
if type_pswrd == '':
    type_pswrd = default_type
if type_pswrd == '1':
    simbols = simbols_no_repeat
if type_pswrd == '2':
    simbols = simbols_repeat
while type_pswrd != '1' and type_pswrd != '2':
    type_pswrd = input_type()
col_pswrd = input_col()
if col_pswrd == '':
    col_pswrd = default_col
while not isinstance(col_pswrd, int):
    try:
        col_pswrd = int(col_pswrd)
    except:
        col_pswrd = input('\n\nВы ввели не число! Какой длины пароль сгенерировать?\n(Меньше 12 не рекомендую, можете оставить по умолчанию, нажав ENTER)\n: ')


def buildpswrd(size):
    return ''.join(random.choice(simbols) for _ in range(size))

print(f'\n\nВаш пароль:\n{buildpswrd(col_pswrd)}')
input('Нажмите ENTER, чтобы выйти из программы: ')