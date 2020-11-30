import itertools

n , k = map(int,input().split())

list_a = [0 for i in range(n)]

c = [i for i in range(2,n+1)]
numlst =[]
lst = []

for i in range(n):
    numlst.append(list(map(int,input().split())))

for i in itertools.permutations(c,len(c)):
    lst.append(list(i))
#print(numlst)
#print(lst)
before =1
ans = 0
count = 0
for i in range(len(lst)):
    before = 1
    ans = 0
    for l in range(len(c)):
        next_a = lst[i][l]
        ans += numlst[before-1][next_a-1]
        before = next_a

        if (l == len(c) - 1):
            ans += numlst[before-1][0]


    if(ans == k):
        count+= 1

print(count)

    


