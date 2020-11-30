
n,m = map(int,input().split())

a = list(map(int,input().split()))

sum_a = sum(a)
count = 0
for i in range(n):

    if (a[i] >= sum_a / (4*m)):
        count += 1


if (count >= m):
    print("Yes")

else:
    print("No")
