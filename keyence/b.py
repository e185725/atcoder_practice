n,k = map(int,input().split())
a = list(map(int,input().split()))

#print(sorted(a))
k =10**3
a = [0]*10**6
num = 0
ans = 0

#print(sorted(a))
#print(10 in a)

for i in range(k):
    num = -1
    while( num+1 in a):
        a.remove(num+1)
        num += 1

    ans += num + 1

print(ans)

