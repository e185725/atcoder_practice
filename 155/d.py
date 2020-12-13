import numpy as np

n, k = [int(x) for x in input().split()]
a = np.array([int(x) for x in input().split()])

a.sort()
neg = a[a < 0]
zero = a[a == 0]
pos = a[a > 0]
print(a)
print(neg,zero,pos)
def count(x):
    ans = 0
    if x >= 0:
        ans += n * len(zero)
    ans += np.searchsorted(a, x//pos, side='right').sum()
    #print(np.searchsorted(a, x//pos, side='right'))
    ans += (n-np.searchsorted(a,-(-x//neg))).sum()
    print(n-np.searchsorted(a,-(-x//neg)))
    ans -= np.count_nonzero(a*a <= x)
    return ans//2

ok = 10**18
ng = -ok-1
while ok - ng > 1:
    cen = (ok + ng) //2
    if count(cen) >= k:
        ok = cen
    else:
        ng = cen
print(ok)