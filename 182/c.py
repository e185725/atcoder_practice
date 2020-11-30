
N = list(map(int,input()))

count_1 = 0
count_2 = 0
count_3 = 0
#print(N)

if (sum(N) % 3 == 0):
    print(0)

elif (sum(N) < 3):
    print(-1)

elif ( len(N) <= 2):
    for n in N :
        if(n % 3 == 0):
            count_3 += 1
    
    if (count_3 >= 1):
        print(1)
    
    else:
        print(-1)

elif(sum(N) % 3 == 1):
    for n in N :
        if(n % 3 == 1):
            count_1 += 1
        elif(n % 3 == 2):
            count_2 += 1
        else:
            pass 
    if(count_1 >= 1):
        print(1)
    elif(count_2 >= 2 ):
        print(2)
    else:
        print(-1)

elif(sum(N) % 3 == 2):
    for n in N :
        if(n % 3 == 1):
            count_1 += 1
        elif(n % 3 == 2):
            count_2 += 1
        else:
            pass 
    if(count_2 >= 1):
        print(1)
    elif(count_1 >= 2):
        print(2)    
    else:
        print(-1)

else: pass

    
   

