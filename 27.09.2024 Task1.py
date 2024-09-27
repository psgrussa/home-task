try:
    print('напишите число, а программа проверит положительное оно или нет')
    chislo = int(input())
    if chislo>0:
        print('Число положительное')
    elif chislo<0:
         print('Число отрицательное')
except:
        print('ошибка при вводе')
