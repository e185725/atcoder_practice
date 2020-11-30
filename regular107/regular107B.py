N,K = map(int,input().split())
K = abs(K)
ans = 0 

for i in range(2,2*N+1):
    
    f = min(i-1,2*N + 1 - i)

    f_2 = min(i+K-1, 2*N + 1 - (i + K) )
    #print(f_2)
    if(f < 0):
        f = 0
    if (f_2 < 0):
        f_2 = 0
    ans += f * f_2

print(ans)