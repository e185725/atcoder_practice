
n,k = map(int,input().split())

p = list(map(int,input().split()))


ans_lst = [0 for i in range(1001)]


for i in range(1,1001):
    ans_lst[i] += ans_lst[i-1] + i


for i in range(1,1001):
    ans_lst[i] /= i

ans_dict = {i:l for i,l in enumerate(ans_lst)}
#print(ans_dict)

ans = 0
ans_ = 0
p_ls = []
for i in range(n):
    p_ls.append(ans_dict[p[i]])


for i in range(n):
    ans_ += p_ls[i]

    if (i >= k-1):
        ans = max(ans,ans_)
        ans_ -= p_ls[i-(k-1)]

        
#print(p_ls)
print(ans)
