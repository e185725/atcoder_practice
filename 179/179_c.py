import math
N = int(input())


A = [i+1 for i in range(10**3)] 
B = [0 for i in range(10**6)] 

count = 0

#print(A)
for a in A:
    for i in range(1,int(math.sqrt(a))):
        if(a % i == 0):
            B[a] += 1

print(B[1:100],A[0])






        


