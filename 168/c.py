import math
a,b,h,m = map(float,input().split())

#print(math.cos(math.radians(60)))

h_tan = 360/12
m_tan = 360/60


cos = abs(h_tan * h - m_tan * m + 0.5*m)
#print(cos)
if (cos > 180):
    cos = 360.0 - cos

ans = a**2 + b**2 - 2*a*b*math.cos(math.radians(cos))
#print(ans)
print(math.sqrt(ans))