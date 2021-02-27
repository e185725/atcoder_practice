
n,k = map(int,input().split())

a = list(map(int,input().split()))

a = sorted(a)

mod = 10**9+7

kaizyou = [ 1 for i in range(1,n+1)]

for i in range(1,n):
    kaizyou[i] *= kaizyou[i-1]*(i+1)
    print(kaizyou)

def conb(a,b):
    if (b < a):
        tmp = b
        b = a
        a = tmp 
    aCb = kaizyou[b-1] // kaizyou[a-1]

    return aCb

print(conb(2,4))

#max_sum

