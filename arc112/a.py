import math

t = int(input())

for i in range(t):
    l,r = map(int,input().split())
    if (l == r and l == 0):
        print(1)
        continue
    if (l == r and l != 0):
        print(0)
        continue
    if (r - l  < r//2 ):
        print(0)
        continue
    a = r - l
    ans = a - l + 1
    
    last_ans = ans * (ans + 1) // 2

    print(last_ans)


"""
5
6 12
0 2
4 9
0 0
12345 12346 


0 1000000
"""