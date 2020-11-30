

S = input()
before = ""
count = 0 
ans = 0
for i in range(len(S)):
    
    if ( S[i] == "R" and count == 0):
        count = 1
    
    elif(S[i] == "R" and before == "R"):
        count += 1
    
    else :
        count = 0

    before = S[i]

    if ( ans < count ):
        ans = count 

print(ans)




    

    


