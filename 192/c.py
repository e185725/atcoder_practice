
n,k = map(int,input().split())

a = n
for i in range(k):

    a = list(str(a))

    b_1 = sorted(a)
    b_2 = sorted(a,reverse=True)
    b_1 = int("".join(b_1))
    b_2 = int("".join(b_2))
    a = b_2 - b_1
print(a)


