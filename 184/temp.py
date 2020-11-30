
n,m,q = map(int,input().split())

n_lst = [ [0 for i in range(n)] for i in range(n)]
n_lst_max  = { i+1 : 0 for i in range(n)}

for i in range(m):
    a,b,f = map(int,input().split())
    a -= 1
    b -= 1
    n_lst[a][b] = f
    n_lst[b][a] = f

for i in range(1,n+1):
    n_lst_max[i] = max(n_lst[i-1])


ans = 0
member_max= []
for i in range(q):
    
    op , int_s = map(str,input().split())
    int_s = int(int_s)

    if ( op == "+"):
        member_max.append(n_lst_max[int_s])
    else:
        if (n_lst_max[int_s] not in member_max):
            pass

        else:
            member_max.remove(n_lst_max[int_s])

    #print(member_max)
    
    if (member_max == []):
        print(0)
    else:
        print(max(member_max))
#print(n_lst)
print(n_lst_max)
        


        




