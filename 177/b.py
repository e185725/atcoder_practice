
S = input()
T = input()
ans_count = 0
for i in range( len(S) - len(T) + 1):
    count = 0
    for  l in range( len(T) ):

        if ( S[i+l] == T[l] ):
            count += 1
    
    if( ans_count < count ):
        ans_count = count

print(len(T) - ans_count)        

        
    