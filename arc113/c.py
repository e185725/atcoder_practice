
s = list(input())
s = s[::-1]
len_s = len(s)

cnt = 0
for i in range(len_s-2):
    if (s[i] == s[i+1] and s[i+1] != s[i+2]):
        s[i+2] = s[i]

        cnt += 1
    else:
        print(i)
print(cnt)
print("".join(s))


