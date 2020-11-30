cnt = 0
s_r = s_l = ""
s = input()
q = int(input())
for _ in range(q):
    n = input().split()
    if n[0] == "1":
        cnt = (cnt + 1) % 2
    else:
        if (int(n[1]) + cnt) % 2:
            s_l += n[2]
        else:
            s_r += n[2]
res = s_l[::-1] + s + s_r
if cnt:
    print(res[::-1])
else:
    print(res)