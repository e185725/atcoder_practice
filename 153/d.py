
import math

h = int(input())
cnt = 0
ans = 0
print()
while (h / 2 != 0):
    h /= 2
    h = math.floor(h)
    ans += 2**cnt
    cnt += 1
print(ans)