

n = int(input())
cnt = 0
for i in range(n):
    s = input()

    if (s == "AND"):
        cnt += 1
    else:
        pass

print(2**(n+1) - 2**(cnt+1))

