n = int(input())

a = list(map(int,input().split()))


before_max = a[0]
humidai = 0
humidai_sum = 0
for i in range(1,n):
    humidai = 0
    if(before_max >= a[i]):
        humidai = before_max - a[i]
        humidai_sum += humidai

    if(before_max < a[i]):
        before_max = a[i]
        

    #print(humidai,before_max,before_max)
print(humidai_sum)