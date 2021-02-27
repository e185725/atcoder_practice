x=input()
M=int(input())
d=int(max(x))
keta=len(x)

if keta==1:
    if int(x)>M:
        print(0)
    else:
        print(1)
    exit()

#########

def serch(n):
    tmp=0
    for i in range(keta):
        tmp+=int(x[i])*n**(keta-i-1)
    if tmp<=M:
        return True
    else:
        return False

left=d
right=M+1
print(left,right)
while right-left>1:
    mid=(left+right)//2
    
    if serch(mid):
        left=mid
    else:
        right=mid

    print(left,right)

print(left-d)