"""
4 4
1 4
4 1
.##.
####
####
.##.
"""
"""
y,x = list(map(int,input().split()))
#全部−1する必要あり
start_y,start_x = list(map(int,input().split()))
end_y , end_x = list(map(int,input().split()))

make_map = []
for i in range(y):
    make_map.append(list(input()))

for i in range(y):
    print(make_map[i])
"""

import sys
input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    
    ch += 1
    cw += 1
    dh += 1
    dw += 1
    
    
    s = ["#"*(w+4)]
    s.append("#"*(w+4))
    for i in range(h):
        s.append("##" + input()[:-1] + "##")
    s.append("#"*(w+4))
    s.append("#"*(w+4))
    
    
    ans = [[-1]*(w+4) for _ in range(h+4)]
    for i in range(h+4):
        for j in range(w+4):
            if s[i][j] == "#":
                ans[i][j] = -2
    ans[ch][cw] = 0
    """
    for i in range(len(ans)):

        print(ans[i])
    >>>
    -2 は壁を表す
    −1 は移動できる点
    0 はスタート地点
    [-2, -2, -2, -2, -2, -2, -2, -2]
    [-2, -2, -2, -2, -2, -2, -2, -2]
    [-2, -2, -1, -2, -2, 0, -2, -2]
    [-2, -2, -2, -2, -2, -2, -2, -2]
    [-2, -2, -2, -2, -2, -2, -2, -2]
    [-2, -2, -1, -2, -2, -1, -2, -2]
    [-2, -2, -2, -2, -2, -2, -2, -2]
    [-2, -2, -2, -2, -2, -2, -2, -2]
    
    """
    #移動A
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #移動B
    move2 = [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), \
             (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), \
             (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), \
             (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), \
             (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]
        
    not_yet = [(ch, cw)]#スタート地点？
    one_time = []
    
    while len(not_yet) > 0:
        x, y = not_yet.pop()
        one_time.append((x, y))

        #移動Aで移動できる点をひたすら移動している
        for (p, q) in move:
            v1, v2 = x+p, y+q
            if ans[v1][v2] == -1:
                not_yet.append((v1, v2))#移動していないリストに追加
                ans[v1][v2] = ans[x][y]#移動地点と同じ値を代入
            
        

        #移動Aを行える点がなくなった 
        if len(not_yet) == 0:

            #移動B再現
            while len(one_time) > 0:
                print(one_time)
                
                x2, y2 = one_time.pop()

                for (v1, v2) in move2:
                    i, j = x2+v1, y2+v2#魔法で移動できる範囲を表す
                    if ans[i][j] == -1:#移動できるなら
                        ans[i][j] = ans[x2][y2]+1#移動できるポイントに移動判定を行なった地点の値+1を返す
                        not_yet.append((i, j))#まだ移動Aを行なっていないリストに追加

        """
        for i in range(len(ans)):
            print(ans[i])
        print()
        """
          
    print(ans[dh][dw])
    
    
    
if __name__ == "__main__":
    main()

