
s,p = map(int,input().split())


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

a = make_divisors(p)

for i in a:
    b = p // i
    if (b + i == s):
        #print(b,i)
        print("Yes")
        exit()

print("No")