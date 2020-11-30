S = input()
Q = int(input())
one_count = 0



def qeury_1(int_a,S):
    if(int_a == "1"):
        S = query[2] + S
        return S    
    else :
        S = S + query[2]
        return S
        
def query_2(int_a,S):

    if(int_a == "2"):
        S = query[2] + S
        return S
    else :
        S = S + query[2]
        return S

for q in range(Q):
    query = list(map(str,input().split()))
    #print(query)
    #print(S)
    if(query[0] == "1"):
        one_count += 1
    else :
        if(one_count % 2== 0 ):
            S = qeury_1(query[1],S)
        else:
            S = query_2(query[1],S)

if (one_count % 2 == 1):
    S =S[::-1]


print(S)