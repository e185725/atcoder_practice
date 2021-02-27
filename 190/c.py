"""
n,m = map(int,input().split())

ab_lst = []
max_a = 0
for i in range(m):
    a,b = map(int,input().split())

    ab_lst.append([a,b])

k = int(input())

k_lst = []
for i in range(k):
    c,d = map(int,input().split())

    k_lst.append([c,d])


kkk_lst =[]

for i in range(2**k):
    a = format(i,"b").rjust(k,"0")
    #print(a)
    kk_lst = []
    for l in range(k):
        kk_lst.append(k_lst[l][int(a[l])])

    #print(set(kk_lst))
    kkk_lst.append(list(set(kk_lst)))

lst = sorted(kkk_lst,key=len ,reverse=True)
#print(lst[0])
max_len = len(lst[0])
#print(max_len)
i = 0
while(True):
    #print(lst[i])
    if(max_len != len(lst[i])):
        print(max_a)
        break



    k_dict = {str(i):0 for i in range(1,n+1)} 

    for l in lst[i]:
        k_dict[str(l)] += 1
    #print(k_dict)
        count = 0
        for c in range(m):
            if (k_dict[str(ab_lst[c][0])] >= 1 and k_dict[str(ab_lst[c][1])] >= 1 ):
                count += 1
    i += 1
    max_a = max(max_a,count)
"""

import itertools

N, M = map(int, input().split())
cond = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
choice = [tuple(map(int, input().split())) for i in range(K)]
ans = 0
print(cond)
print(choice)
for balls in itertools.product(*choice):
    #print(balls)
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in cond)
    print([A in balls and B in balls for A, B in cond])
    #print(cnt)
    if ans < cnt:
        ans = cnt
print(sum([True]))
print(ans)




