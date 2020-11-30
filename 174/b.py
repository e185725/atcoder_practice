import math

N,D = map(int,input().split())
count = 0
for i in range(N):
    x,y = map(int,input().split())

    if( D >= math.sqrt(x**2+y**2)):
        #print(math.sqrt(x**2+y**2))
        count += 1

print(count)

