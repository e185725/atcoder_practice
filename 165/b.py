

n  = 100 

x = int(input())
count = 0
while (n < x):
    n += n // 100
    

    count += 1

print(count)