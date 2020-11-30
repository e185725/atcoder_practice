
"""a = int(input())

import itertools
a_list = [i for i in range(3,a+1)]
#print(a_list)

for i in itertools.combinations_with_replacement(a_list,len(a_list)):
    if(sum(i) == a):
        print(sum(i))
        """

MOD = 10**9 + 7
S = int(input())

dp = [1] * 2001
dp[0] = dp[1] = dp[2] = 0
"""
for i in range(S+1):
    for j in range(3, i):
        dp[i] += dp[i-j]
    print(i,dp[0:S+1])

"""

for i in range(3,S+1):
    for l in range(i+1-3):
        dp[i] += dp[l]

    #print(i,dp[0:i+1])

      

print(dp[S] % MOD)

