import math 

x = int(input())
a = x
x /= 100
x = math.ceil(x)
if (a % 100 == 0):
    print(100)
else:
    print(x * 100 - a)