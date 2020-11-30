

x,n = map(int,input().split() )

p = list(map(int,input().split()))

#print(p.count(0))
ans = x
ans2 = x
while True :
    if(p.count(ans) != 1):
        break
    ans += 1

while True :
    if(p.count(ans2) != 1):
        break
    ans2 -= 1

if (abs(ans2-x) <= abs(ans-x)):
    print(ans2)
else:
    print(ans)
    
    