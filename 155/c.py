

n = int(input())
ans = {}
for i in range(n):
    s = input()

    ans[s] = ans.get(s,0) + 1

ans_sort = sorted(ans.items(), key = lambda x : x[0])
max_ans = max(ans.values())
#print(max_ans)
#print(ans_sort)

for i in ans_sort:
    if (max_ans != i[1]):
        continue

    print(i[0])
        


