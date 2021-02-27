N = int(input())
A = [[0] * 10 for i in range(10)]

for i in range(1,N+1):
    s = str(i)
    front = int(s[0])
    end = int(s[-1])
    A[front][end]+=1

ans = 0

for i in range(10):
  for j in range(10):
    ans+=A[i][j]*A[j][i]

# for i in A:
#     print(i)
print(ans)