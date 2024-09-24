print('Сколько у вас строк на странице?')
stroki = int(input())
print('Сколько у вас символов на одной строке?')
simvoli = int(input())
simvolov_nastanise = stroki*simvoli
print(simvolov_nastanise, 'Символов на одной странице')
simvolov_na2stanise = simvolov_nastanise*2
print(simvolov_na2stanise, 'Символов на двух страницах')
informasiya = simvolov_na2stanise*5
print(informasiya, 'Информации на двух страницах (биты)')
else:
    print('ошибка ввода')
