M=998244353
I=pow(3,M-2,M)
f=lambda:input().split()
r=range
H,W,K=map(int,f())
g=[['.']*W for _ in r(H)]
for _ in r(K):
  h,w,c=f()
  g[int(h)-1][int(w)-1]=c

d=[[0]*-~W for _ in r(H+1)]
d[0][0]=pow(3,H*W-K,M)
print(d[0][0])
for i in r(H):
  for j in r(W):
    s,t=g[i][j],d[i][j]%M
    d[i][j+1]+=t
    d[i+1][j]+=t
    if s=='R': 
        d[i+1][j]-=t
    if s=='D': 
        d[i][j+1]-=t
    if s=='.':
      d[i][j+1]-=t*I
      d[i+1][j]-=t*I
print(d[-2][-2]%M)