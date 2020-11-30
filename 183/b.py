import math

sx,sy,gx,gy = map(int,input().split())

sx,sy = sx,abs(sy)
gx,gy = gx,-abs(gy)

y =   (gy - sy) /(gx - sx)

#y = ax + b
b = sy - y*sx

x = -b / y
print(x)