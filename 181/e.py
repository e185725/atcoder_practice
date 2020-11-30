"""
N,M = map(int,input().split())
H = list(map(int,input().split()))
H = sorted(H)
W = list(map(int,input().split()))
W = sorted(W)
#print(H)
print(W)

ans_last = 10**9
ans = 0
"""
#総当たり式 O(N*M+NlogN) 時間切れ
"""
for i in W:
    H.append(i)
    H = sorted(H)
    ans = 0
    
    for l in range(0,N+2//2,2):
        ans += H[l+1] - H[l]

    if ( ans_last > ans):
        ans_last = ans
    H.remove(i)

    
print(ans_last)

"""

#解答例

import bisect
 
N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()

sum1 = [H[i + 1] - H[i] for i in range(N - 1)]
sum2 = sum1[1::2] + [0]
sum1 = [0] + sum1[::2]

print(sum1)
print(sum2)
#DP
for i in range(len(sum1) - 1):
    sum1[i + 1] += sum1[i]

for i in range(len(sum2) - 1, 0, -1):
    sum2[i - 1] += sum2[i]

print(sum1)
print(sum2)

ans = 1 << 60

for w in W:
    x = bisect.bisect(H, w)
    print(x)
    if x % 2 != 0:
        x -= 1
    
    cost = sum1[x // 2] + sum2[x // 2] + abs(H[x] - w)
    print(sum1[x // 2] , sum2[x // 2] , abs(H[x] - w) )
    if ans > cost:
        ans = cost
print(H)
print(ans)