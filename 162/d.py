
from collections import Counter

n = int(input())
s = input()
count = Counter(s)
ans = count["R"]*count["G"]*count["B"]
anser = 0



for i in range(n):
    for j in range(i + 1, n):
        k = 2 * j - i
        if k < n and s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            ans -= 1

print(ans)





