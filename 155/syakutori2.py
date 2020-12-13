n=12
a=[4,6,7,8,1,2,110,2,4,20,3,9]
x=25

n=10
x=28
a=[5,1,2,5,10,7,4,9,2,8]

right = 0
sum_a=0
ans = 15

for left in range(n):
    while(right < n and sum_a+a[right] < x):
        sum_a += a[right]
        right +=1
    
    if (right + 1 <= n):
        if (sum_a + a[right] >= x):
            #print(right - left + 1)
            ans = min(ans,right - left + 1)

        else:
            pass
    #print(right - left +1)
    sum_a -= a[left]

print(ans)