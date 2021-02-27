
h,w = map(int,input().split())

map_lst  =[]

for i in range(h):
    s_x = list(input())

    map_lst.append(s_x)


#search
#(x,y)
#[y,x]

search = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
yy,xx =0,0
kaku = 0
y_,x_ = 0,0
for i in range(h):
    for l in range(w):

        if (map_lst[i][l] == "#"):
            yy = i
            xx = l


            for y,x in search:
                #print(y,x)
                if (map_lst[yy+y][xx+x] == "#"):
                    #print(i+y,l+x)
                    yy,xx = yy+y,xx+x

                    while (map_lst[yy+y][xx+x] == "#"):
                        yy,xx = yy+y,xx+x
                    
                    kaku += 1
                    #print(">>>",xx,yy,kaku)
            
            if (kaku <= 2):
                print(4)
                exit()

            print(kaku)
            exit()


"""
4 5
....
.##.
.##.
.##.
....

3 3
...
.#.
...

10 10
..........
..##......
..###.....
..#.......
..####....
..####....
..###.....
..##......
..#.......
..........




"""

