"""
import networkx as nx 
g = nx.DiGraph()
g.add_node(1)
g.add_nodes_from([3,4,5])
g.add_edge(2,1)
nx.add_path(g,[1,2,3,4,5])
#nx.nx_agraph.view_pygraphviz(g, prog='fdp')  # pygraphvizが必要
#情報の取得
#頂点の一覧
print(list(g.nodes))
#辺の一覧
print(list(g.edges))
#指定した始点に対する、終点の一覧とへんの一覧
print(list(g.succ[1]),g.out_edges(1))
# 指定した終点に対する、始点の一覧と辺の一覧
print(list(g.pred[5]), g.in_edges(5))

# 指定した頂点に対する、隣接している頂点の数とその一覧
print(g.degree(4), list(nx.all_neighbors(g, 4)))
"""

import networkx as nx 

n,m = map(int,input().split())
g = nx.DiGraph()
for i in range(m):
    a,b = map(int,input().split())
    g.add_edge(a,b)
    g.add_edge(b,a)

#nx.nx_agraph.view_pygraphviz(g, prog='fdp')  # pygraphvizが必要

# 指定した終点に対する、始点の一覧と辺の一覧
print(list(g.pred[1]), g.in_edges(1))
#print(nx.has_path(g,source = 1))
if(len(list(g.pred[1]) ) > 0 ):
    print("Yes")
else:
    print("No")

print(nx.shortest_path(g,target = 1))

for i in range(1,len(nx.shortest_path(g,target = 1))+1):
    if(i == 1):
        continue
    print(len(nx.shortest_path(g,target = 1)[i]) - 1)