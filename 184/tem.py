import random
n = 7
s = "4567654"

n = int(input())
s = input()

#s = [ str(random.randint(1,10)) for i in range(100000)]
#n = len(s)

sum_a = 0
for i in s:
    sum_a += int(i)

mean = sum_a//3
ans = 10
a = 0
b = 0
c = 0
a_lst = []
b_lst = []
c_lst = []
for i in s:
    i = int(i)
    if(a + int(i) < mean):
        a += int(i)
        a_lst.append(i)
    elif(b < mean):
        b += int(i)
        b_lst.append(i)
    else:
        c += int(i)
        c_lst.append(i)
#print(mean)
#print(a,b,c)
#print(a_lst,b_lst,c_lst)
#print()



for i in range(int(1*10**5)):

    
  
    if ((a <= b <= c) and ans > c-a and c-a >= 0):
        ans = c-a
        #print(0,ans)

    if ( a > b ):
        a -= a_lst[-1]
        b += a_lst[-1]
        pop = a_lst.pop(-1)
        b_lst = [pop] + b_lst  

    if ((a <= b <= c) and ans > c-a and c-a >= 0):
        ans = c-a 
        #print(10,ans)


    if ( c < b):
        b -= b_lst[-1]
        c += b_lst[-1]
        pop = b_lst.pop(-1)
        c_lst = [pop] + c_lst
    
    if ((a <= b <= c) and ans > c-a and c-a >= 0):
        ans = c-a
        #print(100,ans)

    if(a < c):
        a += c_lst[-1]
        c -= c_lst[-1]
        pop = c_lst.pop(-1)
        a_lst = [pop] + a_lst


    if ((a <= b <= c) and ans > c-a and c-a >= 0):
        ans = c-a
        #print(1000,ans)

    #print(a_lst,b_lst,c_lst)

    
        



#print(mean)
#print(a,b,c)
#print(a_lst)
#print(b_lst)
#print(c_lst)
print(ans)