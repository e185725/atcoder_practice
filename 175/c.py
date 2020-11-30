import numpy as np
import copy
import sys

X, K, D = map(int, input().split())

X = abs(X)
if (X//D) >= K:
    ans = abs(X-K*D) 
else:
    remain = K - (X//D)
    if remain % 2 == 0:
        ans = X % D
    else:
        ans = abs(X % D - D)
print(ans)