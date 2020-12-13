
#友達候補条件
# 1. a != b
# 2. a and b not block
# 3. a and b not friend
# 4. c_l = b
#    c_0 = a
#    i = 0,1,....,L-1 
#    c_i = c_i+1
#

import sys 

class UnionFind():
    #作りたい要素数nで初期化
    #使用するインスタンス変数の初期化

    def __init__(self,n):
        self.n = n
        #root[x]<0ならそのノードが根かつその値が木の要素数
        #rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        #木をくっつけるときにアンバランスにならないように調節する
        self.rnk = [0]*(n+1)


    def Find_Root(self,x):
        if(self.root[x] < 0):
            return x

        else:
            #ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            
            return self.root[x]

    #木の併合、入力は併合したい各ノード
    def Unite(self,x,y):
        #入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)

        #すでに同じ木に属していた場合
        if(x == y):
            return

        #違う木に属していた場合rnkをみてくっつける方を決める
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            #rnk が同じ（深さに差がない場合)は１増やす
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    # xとyが同じグループに属するか判断
    def isSameGroup(self,x,y):
        return self.Find_Root(x) == self.Find_Root(y)

    #ノードxが属する木のサイズを返す
    def Count(self,x):
        return -self.root[self.Find_Root(x)]

def resolve():
    int1 = lambda x : int(x) -1 
    readline = sys.stdin.readline
    
    n,m,k = map(int,readline().strip().split())

    uf = UnionFind(n)

    exc =[0]*n
    #自節から伸びている枝の数

    for i in range(m):
        a,b = map(int1,readline().strip().split())
        uf.Unite(a,b)
        exc[a]+=1
        exc[b]+=1
    print()
    print(exc)
    print(uf.Count(0),uf.Count(1),uf.Count(2),uf.Count(3),uf.Count(4))
    
    for i in range(k):
        a,b = map(int1,readline().strip().split())
        #同じグループに属していてかつ友人候補なら
        if uf.isSameGroup(a,b):
            exc[a] += 1
            exc[b] += 1

    #出力処理
    for i in range(n):
        if i== (n-1):
            print(uf.Count(i)-1-exc[i])
        
        else:
            print(uf.Count(i)-1-exc[i],end=" ")

resolve()