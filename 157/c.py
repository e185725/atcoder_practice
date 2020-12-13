
import numpy as np 

n,m = map(int,input().split())

ans = ["0" for i in range(n)]
if (len(ans) != 1):
    ans[0] = "1"

change_count = [0 for i in range(n)]
for i in range(m):
    s,c = map(int,input().split())
    if (ans[s-1] != str(c)):
        change_count[s-1] += 1
    ans[s-1] = str(c)

change_count = np.array(change_count)

if(np.any(change_count > 1)):
    print(-1)
    #print(111)
    exit()


ans_final = str(int("".join(ans)))

if (len(ans_final) != len(ans)):
    print(-1)
else:
    print(ans_final)

