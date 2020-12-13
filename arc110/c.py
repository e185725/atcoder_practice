
n = int(input())

p = list(map(int,input().split()))

p_ans = sorted(p)
count = 0
ans_lst = []
pn = []
p_count = [1 for i in range(n-1)]
while (count < 5*10**6):
    if (p_ans == p):
        for i in pn:
            print(i+1)
        exit()
        
    
    for i in range(n-1):
        if (p[i]> p[i+1] and p_count[i] == 1):
            tmp = p[i]
            p[i] = p[i+1]
            p[i+1] = tmp
            p_count[i] -= 1
            pn.append(i)
        count += 1

print(-1)




#print(p_ans==p)