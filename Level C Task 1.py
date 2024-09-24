print('сколько у вас КБ?')
KB = int(input())
MB = KB/1024
print(MB, 'МБ')
BAT = KB*1024
print(BAT, 'Байт')
BT = KB*8192
print(BT, 'Бит')
else:
    print('Ошибка при вводе данных')
