try:
   print('введите 3 числа, а программа выведет большее из них')
   num_1 = int(input())
   num_2 = int(input())
   num_3 = int(input())
   if num_1>num_2 and num_1>num_3:
       print('самым большим числом является', num_1)
   elif num_2>num_1 and num_2>num_3:
       print('самым большим числом является', num_2)
   elif num_3>num_2 and num_3>num_1:
       print('самым большим числом является', num_3)
except:
    print('ошибка при получении данных')