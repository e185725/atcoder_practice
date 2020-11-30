
"""import itertools

n,k = map(int,input().split())

p = list(map(int,input().split()))

ans = 10**9

for i in itertools.combinations(p,k):
    if (ans >= sum(i)):

        ans = sum(i)

print(ans)
"""
n,k = map(int,input().split())

p = list(map(int,input().split()))
p.sort()

print(sum(p[:k]))