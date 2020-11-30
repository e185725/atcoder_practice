

s = input()
s_r = s[::-1]

n = len(s)

a = (n-1) // 2
s_a = s[:a]
s_a_r = s_a[::-1]
#print(s_a)

b = (n+3) // 2
s_b = s[b-1:]
s_b_r = s_b[::-1]
#print(s_b)

if (s == s_r and s_a == s_a_r and s_b == s_b_r):
    print("Yes")

else:
    print("No")

