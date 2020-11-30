import numpy as np
n,m,x = map(int,input().split())

list_a = []
for i in range(n):
    list_a.append( np.array(list(map(int,input().split()))) )




a = 2 **n
ans = np.array([0 for i in range(m+1)])
sum = 10**10
for i in range(a):
    
    b = format(i,"b")
    b = b.rjust(n,"0")
    #print(b)
    ans = np.array([0 for i in range(m+1)])
    for l in range(n):
        
        ans += int(b[l])*list_a[l]

    #print(np.all(ans[1:] >= 10 ))

    if(np.all(ans[1:] >= x ) and sum > ans[0]):
        #print(ans)
        sum = ans[0]

if(sum == 10**10):
    print(-1)
    exit()

print(sum)