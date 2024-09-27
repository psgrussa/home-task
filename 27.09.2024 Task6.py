try:
    print('введите два числа, а программа проверит есть ли среди них чётные числа')
    chislo_1 = int(input())
    chislo_2 = int(input())
    chislo_3 = int(input())
    if chislo_1 % 2 == 0 or chislo_2 % 2 == 0 or chislo_3 % 2 == 0:
        print('Есть чётное число')
    else:
        print('Нет чётного числа')
except:
    print('ошибка при вводе данных')