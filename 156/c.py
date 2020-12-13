
n = int(input())

x = list(map(int,input().split()))

x_max = max(x)

x_min = min(x)
sum_x = 0
ans=10 ** 9
for i in range(x_min,x_max+1):
    sum_x = 0

    for l in x :
        sum_x += (l - i) ** 2


    if (sum_x < ans):
        ans = sum_x


print(ans)
