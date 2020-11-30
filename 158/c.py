

#a = max 100 => a//0.08 => 1250
#b = max 100 => b// 0.1 => 1000
a,b = map(int,input().split())

for i in range(1001):
    if (int(i * 0.08) == a and int(i * 0.1) == b):
        print(i)
        exit()
print(-1)