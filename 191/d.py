from decimal import *
import math

x, y, r = map(Decimal, input().split())

min_x = math.ceil(x-r)
max_x = math.floor(x+r)+1
print(min_x,max_x)
ans = 0
for i in range(min_x, max_x):
    p = (r**2 - (x-i)**2).sqrt()
    #sqrt() はroot平方根
    print(p)
    ans += math.floor(y + p) - math.ceil(y - p) + 1
    print(ans)
#floor 切り捨て
#ceil 切り上げ
#+1 は　0座標
print(int(ans))

