print('На улице тепло?')
teplo = input()

if teplo == 'нет':
    print('На улице идёт дождь?')
    rain = input()

    if rain == 'да':
        print('Оденься потеплее и возьми зонтик')
    elif rain == 'нет':
        print('Оденься потеплее, но зонтик можешь не брать')

elif teplo == 'да':
    print('На улице идёт дождь?')
    dozch = input()
    if dozch == 'нет':
        print('Оденься легко, а зонтик можешь не брать')
    elif dozch == 'да':
        print('Оденься легко, но возьми зонтик')