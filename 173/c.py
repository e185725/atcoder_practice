import copy

H, W, K = map(int, input().split())
a = [list(input()) for i in range(H)]
count2 = 0
for i in range(2 ** H):
    b = copy.deepcopy(a)
    for j in range(H):
        if (i >> j) & 1:
            for k in range(W):
                b[j][k] = "$"
    for p in range(2 ** W):
        count = 0
        c = copy.deepcopy(b)
        for m in range(W):
            if (p >> m) & 1:
                for n in range(H):
                    c[n][m] = "$"
        for x in range(H):
            for y in range(W):
                if c[x][y] == "#":
                    count += 1
        if count == K:
            count2 += 1
print(count2)