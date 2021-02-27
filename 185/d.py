import math


n,m = map(int,input().split())

if (m == 0):
    print(1)
    exit()
a = list(map(int,input().split()))

a = sorted(a)
ans = 0
min_a =10**10

if (n == m ):
    print(0)
    exit()

for i in range(m):
    if ( i == 0):
        min_a = a[i]-1
        if (min_a == 0):
            min_a = 1
    else:
        min_a = min(min_a, a[i] - a[i-1] - 1 )
if (min_a == 0):
    min_a = 1

for i in range(len(a)) :
    if (i == 0):
        if (a[i] == 1):
            pass
        else:
            ans += math.ceil( (a[i]-1) / min_a )
    else:
        ans += math.ceil( (a[i] - a[i-1] - 1) / min_a )

if (n == a[-1]):
    ans += math.ceil( (n - a[-1] ) / min_a )
else:

    ans += math.ceil( (n - a[-1]) / min_a )

print(ans)

  
    
