
N,C = map(int,input().split())
ans = 0
lst_a = []
lst_b = []
for i in range(N):
    a,b,c = map(int,input().split())
    lst_a.append([a,c])
    lst_b.append([b,c])

    #span = b-a + 1
    #print(c*span)
    #ans += min(c*span,C*span)

lst_a = sorted(lst_a)
lst_b =sorted(lst_b)

a = 0
b = 0
ormin = C
c_sum = 0
num  = 0 
print(lst_a)
print(lst_b)
for i in range(2*N):
    print(ans , a , b ,c_sum , num )
    if (num == 0):
        num = lst_a[a][0]
        c_sum += lst_a[a][1]
        a += 1
        continue
    
    if (lst_a[a][0] <= lst_b[b][0] and a != 0):
        span = lst_a[a][0] - num + 1
        num = lst_a[a][0]
        ormin =  min(c_sum,C)
        ans += span*ormin

        c_sum += lst_a[a][1]
        a += 1


        if (a >= N):
            a = 0

    else:
        span = lst_b[b][0] - num + 1
        num = lst_b[b][0]

        
        ormin =  min(c_sum,C)
        ans += span*ormin

        c_sum -= lst_b[b][1]
        b += 1        

        


print(ans , a , b ,c_sum , num)
    
#88206004785464
#64217304046676