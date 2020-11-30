
a,b,c,k = map(int,input().split())
if (a > k):
    ans = k
else:
    ans = a
k -= a +b

if (k <= 0):
    print(ans)
    exit()

ans -= k

print(ans)


