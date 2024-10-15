global PI
PI = 3.14

operation = str(input('площадь и радиус какой фигуры вы хотите узнать? '))
if operation == 'прямоугольника':
    long = int(input('введите длину прямоугольника: '))
    shirina = int(input('введите ширину прямоугольника: '))
    def block(radiys):

        print('радус прямоугольника =', long+shirina+long+shirina)
    block(long)
    def block(ploshad):

        print('площадь прямоугольника =', long*shirina)
    block(long)
elif operation == 'круга':
    radiyys = int(input('ведите радиус круга: '))
    def circle(ploshad_cryga):
        print('площадь круга = ', radiyys*PI)
    circle(radiyys)
elif operation == 'треугольника':
    stor_1 = int(input('введите длину первой стороны: '))
    stor_2 = int(input('введите длину второй стороны: '))
    stor_3 = int(input('введите длину третьей стороны: '))
    def treygolnik(radiys):

        print('радиус треугольника = ', stor_1+stor_2+stor_3)
    treygolnik(stor_1, stor_2, stor_3)
    def treygolnik(ploshad):

        print('площадь треугольника = ', (stor_1*stor_2)//2)
elif operation == 'ромба':
    storona_1 = int(input('введите длину первой стороны ромба: '))
    storona_2 = int(input('введите длину второй стороны ромба: '))
    def romb(perimetr_romi):
        print('периметр ромба = ', storona_1+storona_2+storona_1+storona_2)
    romb(storona_1)
    def romb(ploshad_romi):
        print('площадь ромба = ', (storona_1*storona_2)//2)
    romb(storona_1)