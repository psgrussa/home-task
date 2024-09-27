try:
    print('введите два числа, а программа проверит больше ли эти числа 10')
    chislo_1 = int(input())
    if chislo_1>0:
        print('число является положительным')
    elif chislo_1 == 0:
        print('число - нуль')
    elif chislo_1 < 0:
        print('число отрицательное')
except:
    print('ошибка при вводе данных')