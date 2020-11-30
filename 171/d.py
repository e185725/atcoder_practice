
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

B, C = [0]*Q, [0]*Q
for i in range(Q):
    B[i], C[i] = list(map(int, input().split()))

bucket = [0]*100001
for i in A:
    bucket[i] += 1

sum = sum(A)

for i in range(Q):
    sum += (C[i] - B[i]) * bucket[B[i]]
    bucket[C[i]] += bucket[B[i]]
    bucket[B[i]] = 0
    print(sum)