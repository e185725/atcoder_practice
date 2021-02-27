
h,n = map(int,input().split())

a = list(map(int,input().split()))

sum_a = sum(a)

if (h <= sum_a):
    print("Yes")
else:
    print("No")