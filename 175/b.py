import numpy as np
import copy
import sys

N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
L = np.array(L)
ans = []
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if (L[k] < (L[i] + L[j])) and L[i]!=L[j] and L[j]!=L[k] and L[k]!=L[i]:
                tmp = str(L[i]) + str(L[j]) + str(L[k])
                ans.append(int(tmp))
print(len(ans))


    