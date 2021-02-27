"""
N = int(input())
n = 0
n_lst = []
while (10**12 >= n*(n+1)//2):
    n += 1
    n_lst.append(n*(n+1)//2)

print(len(n_lst))
count = 0
for i in range(len(n_lst)):
    #print(n_lst.count(N-n_lst[-i]))
    count += 2

print(count)
"""
N = int(input())
while N % 2 == 0:
    N //= 2
sq = int(N ** 0.5)
print(sq)
ans = sum(N % i == 0 for i in range(1, sq + 1)) * 2 - (sq * sq == N)
print((sq * sq == N))
"""
A = 2 * 9
(1,9)
(3,3)

1 * 18
9 * 2
3 * 6
3 * 6

重複するパターンがあるため
最後にマイナス１をしている。
"""

print(ans * 2)

