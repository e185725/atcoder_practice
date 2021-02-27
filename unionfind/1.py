
"""
unionfindを理解していく

Union: 二つの集合を一つに併合する
Find :　要素がどの集合に属しているかを判定する
この二つに分かれる
"""

from collections import defaultdict

class UnionFind():

    def __init__(self,n):
        self.n = n 
        self.parents = [-1] * n
        #各要素の親要素の番号を格納するリスト
        #要素が根の場合は-(そのグループの親要素数)を格納する

    def find(self,x):
        #要素xが属するグループの根を返す
        if self.parents[x] < 0 :
            return x 
        
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self,x,y):
        #要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)

        if x == y :
            return 
        
        if self.parents[x] > self.parents[y] :
            x,y = y,x 
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x


uf= UnionFind()


