import math

n = int(input())

mod = 10**9 + 7 
a = list(map(int,input().split()))

ans = 0
ans_2 = 0
lcm = a[0]
for i in a:
    lcm = lcm * i // math.gcd(lcm,i)
    #lcm %= mod

for i in a:
    ans += (lcm // i) 
    ans_2 += (lcm // i) % mod

    #print(ans%mod==ans_2%mod)

print(ans%mod)
