
n,s,d = map(int,input().split())
x_lst = []
y_lst = []
for i in range(n):
    x,y = map(int,input().split())
    x_lst.append(x)
    y_lst.append(y)


for i in range(n):
    if(x_lst[i] >= s or y_lst[i] <= d):
        continue

    print("Yes")
    exit()
print("No")