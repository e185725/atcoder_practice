

a,b,c = map(int,input().split())

a_ = (100 - a) * (a/(a+b+c))
b_ = (100 - b) * (b/(a+b+c))
c_ = (100 - c) * (c/(a+b+c))
print(a_,b_,c_)
print(a_+b_+c_)