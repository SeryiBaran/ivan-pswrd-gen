# Генератор паролей
# Меньше 12 символов пароль слабый, ставьте больше

# Набор символов с похожими друг на друга(i,I,1,l,L):
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

# Набор символов без похожих друг на друга букв (по умолчанию):
# abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789

import random
simbols = list('abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789')

def buildpswrd(size):
    return ''.join(random.choice(simbols) for _ in range(size))

print(f'Ваш пароль:\n{buildpswrd(12)}')
input('Нажмите ENTER, чтобы выйти из программы: ')