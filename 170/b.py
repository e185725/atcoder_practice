

x,y = map(int,input().split())

for i in range(x+1):

    if (y == i * 2 + (x - i) * 4):
        print("Yes")
        exit()

print("No")
