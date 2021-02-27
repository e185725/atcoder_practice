import math
x = input()
x_2 = int(x)
x_1 = [ int(i) for i in x]
x_max= max( x_1 ) + 1

m = input()
judge = int(m)

m_len = len(str(m))
#print(x_max)

cnt = 0
n = x_max

if len(x)==1:
    if int(x)>judge:
        print(0)
    else:
        print(1)
    exit()
while(True):
    s = 1
    ans = 0



    

    for i in reversed(x):
        
        int_i = int(i)
        ans += s * int_i

        s *= x_max
    
    x_max += 1

    if (ans <= judge):
        cnt += 1
        #print(cnt)

    else:
        print(cnt)
        exit()



