factorial = 1
number = int(input())
while number > 1:
    factorial = factorial * number
    number = number - 1
    print(factorial)