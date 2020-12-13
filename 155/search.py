
import numpy as np 

a = np.array([-1,0,0,0,0,0,2,3,4,5])
n = 10
ans = 0
neg = a[a < 0]
zero = a[a == 0]
pos = a[a > 0]
x = 10**10

ans += np.searchsorted(a, x//pos, side='right').sum()
print(np.searchsorted(a, x//pos, side='right'))
print((n-np.searchsorted(a,-(-x//neg))))
print (ans)