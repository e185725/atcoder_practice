N = int(input())
A = list(map(int,input().split()))
M = max(A)
cnt_list = [0]*(M+1)
cnt = 0
for i in A:
    for j in range(i,M+1,i):
        cnt_list[j] += 1
for i in A:
    if cnt_list[i] == 1 :
        cnt += 1
print(cnt)