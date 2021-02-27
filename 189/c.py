
n = int(input())

a = list(map(int,input().split()))

num = 1
ans = 0
for i in range(n):
    
    for l in range(i+1,n):
        if (a[i] > a[l]):
            ans = max(ans,a[i]*(l-i))
            break
        else:
            if (l+1 == n):
              ans = max(ans,a[i]*(l-i+1)) 

            pass
    #print(num)
    
    print(ans)
print(ans)

"""
11
2 4 4 9 4 3 9 3 3 3 3 
"""
