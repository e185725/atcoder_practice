
n,x = map(int,input().split())
x = float(x)
ans = 0.0
for i in range(n):
    v,p = map(int,input().split())

    ans += v * p / 100
    #print(v * p / 100,v * (p / 100 ) )
    if (ans > x):
        print(i + 1)
        exit()

print(-1)
"""
3 1000000
1000 100
1000 100
1000 1000000000
"""

