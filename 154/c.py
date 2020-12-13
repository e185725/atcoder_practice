
n = int(input())

a = list(map(int,input().split()))


a_len = len(a)

a = set(a)

a_len1 =len(a)

if (a_len == a_len1):
    print("YES")

else:
    print("NO")