

n=7
a=[1,2,1,3,1,4,4]
a += [0]
num = 0
ans_lst = []
ans = 0
for i in range(n):

    while(ans_lst.count(a[num]) != 1 and num < n):
        ans_lst.append(a[num])
        num += 1
    print(ans_lst)
    ans = max(ans,len(ans_lst))
    ans_lst.pop(0)
    
print(ans)


