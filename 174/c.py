
k = int(input())


res = 7

for i in range(1, 10**6+1):
    #print(res)
    if res % k == 0:
        print(i)
        quit()
    else:
        res %= k
        res = res * 10 + 7

print(-1)