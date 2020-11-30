
X,Y,A,B = map(int,input().split())

ans = 0 

while A*X <= X+B and A*X<Y :

    X *= A
    ans += 1

print(ans + (Y - X -1) // B) 
print( (Y - X -1) // B)
print( (Y - X -1) / B)
print( (Y - X -1) )

#1 1000000000000000000 10 1000000000

print(999999998999999999//10**9)
print(999999998999999999/10**9)