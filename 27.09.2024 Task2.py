try:
    print('введите число, а программа проверит чётное оно или нет')
    chislo = int(input())
    if chislo % 2 == 0:
        print('число чётное')
    elif chislo % 2 != 0:
        print('число нечётное')
except:
    print('числа вводи')