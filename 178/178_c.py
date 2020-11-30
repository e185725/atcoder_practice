a = int(input())


x = 10 ** a 
y = 9 ** a
z = 9 ** a
q = 8 ** a

ans = ( x - y - z + q ) % (10 ** 9 + 7 )

print(ans)