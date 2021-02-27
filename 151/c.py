

n , m = map(int,input().split())

ac_dict = {str(i) : 0 for i in range( 1,n+1 ) }

wa_dict =  {str(i) : 0 for i in range( 1,n+1 ) }


for i in range(m):

    p,s = map(str,input().split())

    if (s == "WA" and ac_dict[p] == 0):
        wa_dict[p] += 1

    elif(s == "AC" and ac_dict[p] == 0):
        ac_dict[p] += 1

    else:
        pass

for i in range(1,n+1):
    if (ac_dict[str(i)] == 0):
        wa_dict[str(i)] = 0

print(sum(ac_dict.values()),sum(wa_dict.values()))




