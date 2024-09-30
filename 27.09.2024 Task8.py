try:
   print('придумайте имя пользователя')
   username = input()
   print('придумайте свой пароль')
   password = input()
   print('введите имя пользователя')
   username_test = input()
   print('введите ваш пароль')
   password_test = input()
   if password_test == password and username_test == username:
        print('доступ разрешён')
   else:
        print('доступ запрещён')
except:
    print('ошибка при получении данных пользователей')