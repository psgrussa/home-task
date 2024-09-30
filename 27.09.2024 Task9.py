try:
   print('введит любой год, а программа напишет является ли он високосным')
   year = int(input())
   if year%4 or year%400 and year %100 !=0:
         print('год - високоный')
   else:
         print('год не високосный')
except:
    print('ошибка при получении данных')