mx=400001
*p,=range(mx)#0~mxまでの値が入った配列を作成できる
#枝の根を現すことになる
r=[0]*mx
cnt = [1]*mx

def par(x):
    if p[x]==x:
        return x
    res = p[x]=par(p[x])
    return res

def union(x,y):
    px=par(x);py=par(y)
    print(px,py)
    if px==py:
        return
    if r[px]>r[py]:
        p[py]=px
        r[py]+=1
    elif r[px]<r[py]:　
        p[px]=py
        r[px]+=1
    else:#ifと一緒
        p[px]=py
        r[py]+=1
    



n=int(input())

g=[[] for _ in range(mx)]
e=[]
col=set()
for i in range(n):
    ai,bi=map(int, input().split())
    union(ai,bi)
    e.append((ai))
cnt=[0]*mx
for i in range(mx):
    cnt[par(i)]+=1
# 閉路+閉路と連結：全て
# 他：-1
e_cnt=[0]*mx

for ai in e:
    e_cnt[par(ai)]+=1

ans=0
pars=set(par(i) for i in range(mx))
for pi in pars:
    if e_cnt[pi]>=cnt[pi]:
        ans+=cnt[pi]
    else:
        ans+=cnt[pi]-1

print(ans)


