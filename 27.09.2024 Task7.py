try:
    print('введите число, а программа выведет сообщение \n Меньше 10 \n Между 10 и 20 \n Больше 20')
    chislo_1 = int(input())
    if chislo_1<10:
        print('Меньше 10')
    elif chislo_1>10 and chislo_1<20:
        print('Между 10 и 20')
    elif chislo_1>20:
        print('Больше 20')
    else:
        print('число либо 10 либо 20')
except:
    print('ошибка при вводе данных')