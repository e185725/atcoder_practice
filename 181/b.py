N = int(input())

sum_ans = 0

for n in range(N):

    A,B = map(int,input().split())
    A -= 1
    sum_ans += 0.5 *  ( (B * (B+1) ) - (A * (A+1) ) )

print(int(sum_ans))
