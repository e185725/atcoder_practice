import itertools

n,m,q = map(int,input().split())

#n= 10
#m = 10
m_lst = [i for i in range(1,m+1)]
#combinatons_with_replacement
cwr = list(itertools.combinations_with_replacement(m_lst,n))
cwr.sort(reverse = True)
#print(type(cwr[0]))
#print(len(cwr))
q_list =[]

for i in range(q):
    lst = list( map(int,input().split()))

    q_list.append(lst)


ans = 0
for i in range(len(cwr)):
    sum_a = 0
    for l in range(len(q_list)):
        
        #無駄な変数変換があったことで時間を超えてしまった
        #a = q_list[l][0] -1
        #b = q_list[l][1] -1 
        #c = q_list[l][2]
        #d = q_list[l][3]

        if (cwr[i][q_list[l][1] -1] - cwr[i][q_list[l][0] -1] == q_list[l][2]):
            sum_a += q_list[l][3]

    if(ans < sum_a ):
        ans = sum_a

print(ans)
        

