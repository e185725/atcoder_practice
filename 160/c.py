

k,n = map(int,input().split())

a_lst = list(map(int,input().split()))

a_diff = []
for i in range(-1, n-1) :

    if (i == -1):
        if (abs(k + a_lst[i+1] - a_lst[i]) <= abs(a_lst[i] - a_lst[i+1]) ):

            a_diff.append(abs(k + a_lst[i+1] - a_lst[i]))
            
        else:
            a_diff.append(abs(a_lst[i] - a_lst[i+1]))

    else:
        a_diff.append( a_lst[i+1] - a_lst[i])
#print(a_diff)
a_diff.sort()
ans = sum(a_diff[:-1])
print(ans)
