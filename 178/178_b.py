a = list(map(int,input().split()))
a_1,a_2 = [],[]
a_1.append(a[0])
a_1.append(a[1])
a_2.append(a[2])
a_2.append(a[3])

#print(a_1,a_2)
max_a = -(10**30)
for i in a_1:
    for l in a_2:
        if(i*l > max_a):
            max_a = i*l

print(max_a)

