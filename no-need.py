N, K = 7,20
a=[1,1,3,7,8,8,10,20]
a.sort()
ans = N
t = 0
for i in range(N-1, -1, -1) :
    print(a[i])
    if t+a[i] < K:
        t += a[i]
    else:
        ans = min(ans, i)

    #print(ans)
print(ans)
