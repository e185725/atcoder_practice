import numpy as np 
n,k = map(int,input().split())

ans = np.array([0 for i in range(n)])
for i in range(k):

    d = int(input())
    list_a = list(map(int,input().split()))

    for i in list_a:
        ans[i - 1 ] += 1

print(np.count_nonzero(ans == 0)) 

