
k = int(input())

ans = [i for i in range(1,10)]


def lunlun(num , ans ):

    ans = ans

    if (num < 3234566667):

        
        if ( num % 10 == 0):
            pass
        else:
            ans.append(num * 10 + num % 10 - 1)
            lunlun(num * 10 + num % 10 - 1,ans)

        ans.append(num * 10 + num % 10 )
        lunlun(num * 10 + num % 10,ans)

        if (num % 10 == 9):
            pass
        else:
            ans.append(num * 10 + num % 10 + 1)
            lunlun(num * 10 + num % 10 + 1,ans)
            
        
    else:
        pass

    return ans
for i in range(1,10):
    lunlun(i,ans)
ans = list(set(ans))
ans.sort()

print(ans[k-1])
#print(len(ans))

    
    

