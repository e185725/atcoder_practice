

N = int(input())

A = list(map(int,input().split()))
ans = 0
count = 0
ans_s = 0
for i in range(2,1001):
    count = 0
    for l in range(N):
        if (A[l] % i == 0):
            count += 1

    if (ans <= count):
        ans = count
        ans_s = i


print(ans_s)


