import numpy as np 

n,m = map(int,input().split())

h = np.array(list(map(int,input().split())))

h_road_lst = [ [] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())

    h_road_lst[a-1].append(h[b-1])
    h_road_lst[b-1].append(h[a-1])


#print(h_road_lst)
h_road_lst = np.array(h_road_lst,dtype=object)

count = 0
for i in range(len(h_road_lst)):
    if(np.all(h_road_lst[i] < h[i]) or len(h_road_lst[i]) == 0):
        #print(h_road_lst[i])
        count += 1

print(count)