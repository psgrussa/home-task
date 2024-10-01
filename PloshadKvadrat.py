print('введите длину фигуры')
dlina = int(input())
print('введите ширину фигуры')
shirina = int(input())
print('площадь какой фигуры вы хотите вычислить?')
figura = input()
if figura == 'квадрат':
    ploshad_kvadrat = dlina*shirina
    print(ploshad_kvadrat)