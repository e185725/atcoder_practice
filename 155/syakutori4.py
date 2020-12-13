
n=5
a=[1,2,3,2,1]

right = 0

simple_a = a[0] -1 
ans = 0
for left in range(n):
    if (right - left == 0):
        simple_a = -10**10

    while(right < n and simple_a < a[right]):
        simple_a = a[right]
        right += 1
    #print(right-left)
    ans += right - left 
    


print(ans)

