"""N,M = map(int, input().split())

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


list_ans = []
list_dict = {str(i):0 for i in range(N)}
for i in range(M):
    list_a = list(map(int,input().split()))
    list_a.sort()
    list_ans.append(list_a)

list_ans = get_unique_list(list_ans)

ans = 0 

for i in list_ans:
    list_dict[str(i[0])] += 1

print(max(list_dict.values()) +1)
"""
import networkx as nx
import matplotlib.pyplot as plt 

n,m=map(int,input().split())
if m==0:print(1);exit()
a=[[i for i in input().split()] for _ in range(m)]
g=nx.Graph()
for x in a:
     g.add_edge(x[0],x[1])
print(len(max(nx.connected_components(g),key=len)))

