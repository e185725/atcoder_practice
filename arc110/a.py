


n = 30
ans = 1
for i in range(2,n+1):
    ans *= i

ans = ans // (2**22)
ans = ans // (3**11)
ans = ans // (5**5)
ans = ans // (7**3)
ans = ans // (11**1)
ans = ans // (13**1)
ans += 1

for i in range(2,n+1):
    
    pass
    #print(ans % i)
print(ans)
#print(10**13)

#print([i for i in range(2,31)])