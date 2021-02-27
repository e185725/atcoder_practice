import collections
n,x = map(int,input().split())

a = list(map(int,input().split()))
cnt = 0
for i in a:
    if (i != x):
        cnt += 1
        print(i , end=" ")

if (cnt == 0):
    print(" ")       
