import collections
n,k = map(int,input().split())
a = list(map(int,input().split()))

c = collections.Counter(a)
#print(sorted(c))

num = 0
cnt = 0
ans = 0
c_sorted = sorted(c.items(),key=lambda x:x[0])
for i in c_sorted:
    #print(c.items())
    if (num == i[0]):
        
        if (cnt < i[1] and num > 0):
            pass
        else:
            cnt = min(i[1],k)
            #cnt = i[1]
        num += 1
        ans += cnt

    else:
        break
    
print(ans)
"""
21 4
6 2 6 8 4 5 5 8 4 1 7 8 0 3 6 1 1 8 3 0 0   

"""