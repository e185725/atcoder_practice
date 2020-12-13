

n=7
K=6
a=[4,3,1,1,2,10,2]

right = 0
sum_a = 1
max_a = 0

if (a.count(0) != 0):
    print(0)
    exit()
    
for left in range(n):

    while(right < n and sum_a*a[right] <= K):
        
        sum_a *= a[right]
        right += 1
    max_a = max(right-left,max_a)

    sum_a //= a[left]


print(max_a)
    


