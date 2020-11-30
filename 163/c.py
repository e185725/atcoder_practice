
n = int(input())

no_list = { i : 0 for i in range(1,n+1) }

a = list( map( int,input().split() ) )

for i in a:
    no_list[i] += 1

for i in no_list:
    print(no_list[i])
