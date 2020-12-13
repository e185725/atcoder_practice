

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7

ans = pow(2, n, mod)-1

aCn= 1
bCn= 1

for i in range(n-a+1,n+1):
    aCn *= i
    aCn %= mod

for i in range(1,a+1):
    aCn *= pow(i,mod-2,mod)
    aCn %= mod

for i in range(n-b+1,n+1):
    bCn *= i
    bCn %= mod

for i in range(1,b+1):
    bCn *= pow(i,mod-2,mod)
    bCn %= mod


#print(pow(2,-2))
ans -= aCn+bCn
print(ans % mod)