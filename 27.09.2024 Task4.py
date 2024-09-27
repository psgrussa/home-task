try:
    print('введите два числа, а программа проверит больше ли эти числа 10')
    chislo_1 = int(input())
    chislo_2 = int(input())
    if chislo_1 > 10 and chislo_2 > 10:
        print('оба числа больше 10')
    elif chislo_1 > 10 and chislo_2 < 10:
        print('первое число больше 10, а второе меньше 10')
    elif chislo_1 < 10 and chislo_2 > 10:
        print('первое число меньше 10, а второе больше 10')
    else:
        print('одно из чисел - 10')
except:
    print('ошибка при вводе данных')