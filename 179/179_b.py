c = int(input())
count = 0

d = [list(map(int,input().split())) for i in range(c)]
for i in range(c):
    a,b = d[i][0],d[i][1]
    
    if (a==b):
        count += 1
        if ( count == 3):
            break
    else : 
        count = 0

if (count >= 3):
        
    print("Yes")
else :
    print("No")
