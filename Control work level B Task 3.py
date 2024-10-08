import random
from random import  randint
numb = int(input('сколько чисел должно быть? '))
elem = []
for i in range(numb):
    elem.append(random.randint(0, numb))
    list = sorted(elem)
    print(list)
def binary_seach(data, elem):
 elem = 3,6,9
 low = 0
 high = len(data) - 1

 while low <= high:

     middle = (low + high)//2
     if data[middle] == elem:
         return middle
     elif data[middle] > elem:
         high = middle - 1
     else:
         low = middle + 1

 return -1