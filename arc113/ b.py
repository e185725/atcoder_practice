

a,b,c, = map(int,input().split())

def mpower(a, b, n):
    if b==0:
        return 1
    if b==1:
        return a%n
    a1=a
    k=1
    while a1<n and k<b:
        a1=a1*a
        k=k+1

    a1=a1%n
    b1=b//k
    a2=a
    b2=b%k
    return (mpower(a1,b1,n)*mpower(a2,b2,n))%n

#print(mpower(b,c,10))
h = mpower(b,c,8)
d = b % 10
e = c % 10 
ans = a ** d
a_lst = []



for i in range(8):
    #print(a**(i+1))
    a_s = str(a**(i+1))
    a_lst.append(a_s[-1])

f = d*e % 10 
#print(h)
print(a_lst[h-1])




