h, w = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0
for x in range(1, h):
    for y in range(1, w):
        tmp = 0
        if s[x][y] == "#":
            tmp += 1
        if s[x-1][y] == "#":
            tmp += 1
        if s[x][y-1] == "#":
            tmp += 1
        if s[x-1][y-1] == "#":
            tmp += 1
        if tmp == 3 or tmp == 1:
            ans += 1

print(ans)

