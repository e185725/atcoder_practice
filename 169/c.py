from decimal import *

a,b = map(Decimal,input().split())
"""
if (int(a) == 0):
    print(0)
    exit()
a = str(int(a))
a = a[::-1]
b *= 100
b = int(b)
ans = 0



for i in range(len(a)):
    ans += int(a[i]) *(10**i) * b
"""


a= int(a)
b *= 100
b = int(b)
c = a * b
c = c//100
c = int(c)
print(c)


#print(ans//100)

