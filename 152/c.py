
n = int(input())

a = list(map(int,input().split()))
cnt = 0
min_a = 10**9
for i in range(len(a)):

    min_a = min(min_a,a[i])

    if (a[i] <= min_a):
        cnt += 1

print(cnt)