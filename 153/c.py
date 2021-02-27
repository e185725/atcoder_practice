

n,k = map(int,input().split())

h = list(map(int,input().split()))

h = sorted(h)

k = min(n,k)
for i in range(k):

    h.pop(-1)
print(sum(h))