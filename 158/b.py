
n,a,b = map(int,input().split())

if (n % (a+b) < a):
    print( n % (a+b) + n // (a+b) * a )

else:
    print( a + n // (a+b) * a )