#n=int(input())
#p=list(map(int,input().split()))

p = [3,1,2,5,4]
n = 5

if p[0]==1 or p[-1]==n:
    print(-1)
    exit()

pin=0

for i in range(n):
    print(p)
    if p[i]>pin:
        pin=p[i]
        p[i]=-1
    
    else:
        continue

pin=1
ans=[]
for i in range(n):
    if p[i]==-1:
        continue
    elif pin!=p[i]:
        print(*ans,sep='\n')
        print(-1,i)
        exit()
    else:
        for j in range(i,pin-1,-1):
            ans.append(j)
        pin=i+1



print(*ans,sep='\n')



