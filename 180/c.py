import math
N = int(input())
d = int(math.sqrt(N)) + 1
ans = []
ans_2 = []
#print(d)
for i in range(1,d):
    if (N % i == 0):
        ans.append(i)
        if(i != int(N/i)):
            ans_2.append(int(N/i))
for ans in ans:

    print(ans)
for ans_2 in reversed(ans_2):

    print(ans_2)

