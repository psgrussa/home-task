def factorial_number():
    fact = 1
    n = int(input())
    for i in range(2,n+1):
      fact *= i
      print(fact)
factorial_number()