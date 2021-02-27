
n = int(input())

num_dict = {}
num_list = []
double_dict = {}
cnt = 0
for i in range(n):
    a,b = map(str,input().split())
    
    """重複処理ができなかった"""
    if (a == b ):
        if a in double_dict :
            double_dict[a] += 1
        else:
            double_dict[a] = 0
                
    
    if a in num_dict :
        num_dict[a] += 1
    else:
        num_dict[a] = 1

    if b in num_dict :
        num_dict[b] += 1 
    else:
        num_dict[b] = 1
    
    num_list.append([a,b])



ans = len(num_dict)
#print(min(ans,n))


for i in range(len(num_list)):
    if (num_dict[ num_list[i][0] ] == num_dict[ num_list[i][1] ] and num_dict[ num_list[i][1] ] == 1):
        ans -= 1

print(double_dict.values())
print(num_dict)

for i in list(double_dict):
    if (int(i) > 0):
        cnt += 1

    
if (min(ans-cnt,n) == 0):
    print(1)
    exit()
print(min(ans-cnt,n))

print(cnt,ans)
"""
7
3 3
3 3
3 3
2 4
2 4
6 5
4 4 

"""






