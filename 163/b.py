
n,m = map(int,input().split())

a = list( map(int,input().split()) )

for i in a:
    n -= i

    if(n < 0):
        print(-1)
        exit()

print(n)