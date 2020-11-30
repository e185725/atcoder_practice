H,W,m = map (int, input().split())
map_bom = [[0 for i in range(W)] for i in range(H)]
list_a = []
for i in range(m):
    y,x = list(map(int,input().split()))
    y -= 1
    x -= 1
    list_a.append([y,x])
    map_bom[y][x] += 1

for i in range(m):
    print(list_a)
    y = list_a[i][0]
    x = list_a[i][1]
    #x上
    if(y -1 >= 0):
        if( map_bom[y-1][x] != 0):
            map_bom[y][x] += 1

    if(y + 1 < H ):
        if( map_bom[y+1][x] != 0):
            map_bom[y][x] += 1
    
    if(x - 1 >= 0 ):
        if( map_bom[y][x-1] != 0):
            map_bom[y][x] += 1

    if(x + 1 < W ):
        if( map_bom[y][x+1] != 0):
            map_bom[y][x] += 1
ans = 0
ans_lis = []


for h in range(H):
    for w in range(W):
        ans = 0
        if( map_bom[h][w] == 0):

            if(h -1 >= 0):
                if( map_bom[h-1][w] != 0):
                    ans += map_bom[h-1][w] 

            if(h +1 < H):
                if( map_bom[h+1][w] != 0):
                    ans += map_bom[h+1][w] 

            if(w -1 >= 0):
                if( map_bom[h][w-1] != 0):
                    ans += map_bom[h][w-1] 

            if(w +1 < W):
                if( map_bom[h][w+1] != 0):
                    ans += map_bom[h][w+1] 

        ans_lis.append(ans)



                



            

    

for i in range(len(map_bom)):
    print(map_bom[i])

print(ans_lis)