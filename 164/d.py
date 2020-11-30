

# 2*10 **5
# S 1~9

m = 2019
s = [str(i) for i in input()]
s = s[::-1]
n = len(s)
cnt = {i:0 for i in range(m)}
x = 1
total = 0
ans = 0
print(s)
for i in range(n):
    cnt[total] += 1
    total = (total + int(s[i]) * x) % 2019
    ans += cnt[total]
    x = (10*x)% 2019
    print(total,x)
print(ans)





