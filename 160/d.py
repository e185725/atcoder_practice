

N, X, Y = map(int, input().split())

ans = [0] * N

for a in range(1, N+1):
    for b in range(a+1, N+1):
        t = b - a
        t2 = abs(X-a) + abs(Y-b) + 1
        t = t if t < t2 else t2#この書き方良いw
        ans[t] += 1

for i in range(1, N):
    print(ans[i])