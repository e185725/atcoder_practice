"""
#O(CT)

import numpy as np 
n,w = map(int,input().split())

lst = np.array([w]*(2*10**5 + 1))

#lst[0:2] += 1

for i in range(n):
    s,t,p = map(int,input().split())
    lst[s:t] -= p

    #print(lst[:10])   
    if(np.any(lst < 0)):
        print("No")
        exit()

print("Yes")
"""

#O(C+T)

n,w = map(int,input().split())

list_w = [0 for i in range(2*10**5+1)]

for i in range(n):
    s,t,p = map(int,input().split())

    list_w[s] += p
    list_w[t] -= p

#print(list_w)
for i in range(len(list_w)):
    if (i > 0):
        list_w[i] += list_w[i-1]
    #print(list_w)
    #print(max(list_w))

if (max(list_w) > w):
    print("No")

else:
    print("Yes")