mod = 10**9+7
N, K = map(int, input().split())
ans = 0

n = N
for i in range(K, N+2):
    ans += (  ( (n*(n+1) //2 - (n-i)*(n-i+1) //2)  - i*(i-1)//2 + 1))

print(ans  % mod)
"""
max_2 = 3+2 (n*(n+1) //2 - (n-i)*(n-i+1) //2)
min_2 = 0+1
con_2 = 5

max_3 = 3+2+1
min_3 = 0+1+2
con_3 = 4

max_4 = 3+2+1+0
min_4 = 0+1+2+3
con_4 = 1n
"""
#このことから　con_n = sum( max_n - min_n + 1 )
#sum(n_list[n_len - i:]) = n_len*(n_len+1) // 2 - (n_len-i)*(n_len-i+1)//2
#sum(n_list[:i]) = (i-1)*(i) // 2

