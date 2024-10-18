n = int(input())
num = 1
def rec(num):
    if num < n:
        print(num+0)
        rec(num+1)
rec(num)