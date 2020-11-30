n = int(input())
x_y = []
for i in range(n):
    x,y = map(int,input().split())

    x_y.append([x,y])

#print(x_y)
count_list = []
map_list = []

#print( sorted(x_y, key=lambda x: x[1]) ) 
for i in range(n):
    count = 1
    m_l = []
    for l in range(n):

        
        if ( (x_y[i][0] > x_y[l][0] and x_y[i][1] > x_y[l][1]) or (x_y[i][0] < x_y[l][0] and x_y[i][1] < x_y[l][1]) ):
            count += 1
            m_l.append(x_y[l])
    map_list.append(m_l)
    count_list.append(count)
    
    #print(count_list)

print(map_list)

