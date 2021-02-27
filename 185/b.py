
n,m,t = map(int,input().split())
n_n  = n
before_a = 0
before_b = 0
for i in range(m):
    a,b = map(int,input().split())
    
    n -= a - before_b
    before_a = a
    if (n <= 0):
        
        print("No")
        #print(n)

        exit()

    n += b-a
    if (n >= n_n):
        n = n_n
    before_b = b
    #sprint(n)

    if (i == m - 1):
        n -= t-b

        if (n <= 0):
            print("No")
            exit()
print("Yes")
