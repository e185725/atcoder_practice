

"""
この尺取り方は連続した数列を解くことができる。
"""
a=[4,6,7,8,1,2,110,2,4,12,3,9]
a=[5,3,8,6,1,4]


n= len(a)
x = 25
x = 11
right = 0
#legt = 0
sum_a = 0
ans = 0
for left in range(n):
    #sum_a = 0
    while(right < n and sum_a+a[right] <= x):
        sum_a += a[right]
        right += 1
        
    print(right - left)
    ans += right - left 
    sum_a -= a[left]

print(ans)
    
