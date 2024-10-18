a = int(input())
b = int(input())
def task2(a, b):
   if a<b:
      task2(a, b - 1)
      print(b)
   elif a>b:
      print(a)
      task2(a - 1, b)
   else:
      print(a)
task2 (a, b)