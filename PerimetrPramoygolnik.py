print('введите длину фигуры')
dlina = int(input())
print('введите ширину фигуры')
shirina = int(input())
if dlina == shirina:
    print('это не прямоугольник!')
else:
    perimetr = dlina+shirina
    perimetr_2 = perimetr*2
    print(perimetr_2)