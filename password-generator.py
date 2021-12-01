import random

default_type = '1'
default_col = 12
simbols_no_repeat = list('abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789')
simbols_repeat = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
simbols_no_repeat_spec = list('abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789!#')
simbols_repeat_spec = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#')
simbols_no_repeat_all = list('abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789!@#%"&*()_-+={}<>?|:[].~')
simbols_repeat_all = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#%"&*()_-+={}<>?|:[].~')

def input_type():
    type_pswrd_loc = input(u'Список наборов:\nabcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\nabcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789!#\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#\nabcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789!@#%"&*()_-+={}<>?|:[].~\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#%"&*()_-+={}<>?|:[].~\n\n\n--------------------\nПрочитай внимательно!\nПохожие друг на друга - l, L, 1, I, i.\nВнимание! Не все сервисы/сайты/программы принимают пароли со спецсимволами!\nПароли с "!" и "#" работают во всех сервисах/сайтах/программах.\n--------------------\n\n\nКакой набор символов использовать?\n1. Нужен пароль без похожих букв\n2. Нужен пароль с похожими буквами\n3. Нужен пароль без похожих букв с "!" и "#"\n4. Нужен пароль с похожими буквами и с "!" и "#"\n5. Нужен пароль без похожих букв со всеми спец-символами\n6. Нужен пароль с похожими буквами со всеми спец-символами\n\n(Можете оставить по умолчанию 1, нажав ENTER)\n: ')
    return type_pswrd_loc
def input_col():
    col_pswrd_loc = input(f'\n\nКакой длины пароль сгенерировать?\n(Меньше {default_col} не рекомендую, можете оставить по умолчанию {default_col}, нажав ENTER)\n: ')
    return col_pswrd_loc



type_pswrd = input_type()
if type_pswrd == '':
    type_pswrd = default_type
if type_pswrd == '1':
    simbols = simbols_no_repeat
elif type_pswrd == '2':
    simbols = simbols_repeat
elif type_pswrd == '3':
    simbols = simbols_no_repeat_spec
elif type_pswrd == '4':
    simbols = simbols_repeat_spec
elif type_pswrd == '5':
    simbols = simbols_no_repeat_all
elif type_pswrd == '6':
    simbols = simbols_repeat_all
while type_pswrd != '1' and type_pswrd != '2' and type_pswrd != '3' and type_pswrd != '4' and type_pswrd != '5' and type_pswrd != '6':
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