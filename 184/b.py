
n,x = map(int,input().split())

s = list(input())

ans = x

for i in s:
    
    if(i == "o"):
        ans += 1

    else:
        ans -= 1

    if (ans < 0):
        ans = 0
print(ans)