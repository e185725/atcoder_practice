
b,c = map(int,input().split())


if (b == 0 and c == 1):
    print(1)
    exit()

ans = 1

#bが正のの場合
#7simulation
if (b >= 0):
    shou = c // 3
    amari = c % 3

    #0~b
    min_shou = min(b,shou)
    min_shou -= 1
    shou -= 1
    print(shou,amari,min_shou)
    if (min_shou == b-1):
        min_shou = max(0,min_shou)
        ans += min_shou * 2 + 1
    
    elif(amari == 0):
        ans += min_shou * 2
        ans += 1
    elif(amari == 1):
        ans += min_shou * 2
        ans += 2
    elif(amari == 2):
        ans += min_shou * 2
        ans += 3
    else:
        pass

    #b~

    if (amari == 0):
        ans += shou * 2
        ans += 1
    elif(amari == 1):
        ans += shou * 2
        ans += 2
    elif(amari == 2):
        ans += shou * 2
        ans += 3


    


    
    

print(ans)








