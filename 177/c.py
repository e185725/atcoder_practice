
N = int(input())

list_a = list( map( int,input().split() ) )
list_a.sort()
#print(list_a)

list_b = list_a.copy()

#累積和
for i in range (N-1, 0, -1):
    list_b[i-1] += list_b[i]

#print(list_b)

ans = 0 
for i in range(N-1) :
    ans += list_a[i] * list_b[i + 1]


print(ans % (10**9 + 7))


