
import numpy as np 

a = list(map(int,input().split()))
a_1 = list(map(int,input().split()))
a_2 = list(map(int,input().split()))

a = np.array([a,a_1,a_2])

n = int(input())
new_bingo = np.zeros_like(a)
for i in range(n):
    new_bingo[a == int(input())] = 1


#print(new_bingo)


for i in range(3):
    if (new_bingo.sum(axis=1)[i] == 3):
        print("Yes")
        exit()

for i in range(3):
    if (new_bingo.sum(axis=0)[i] == 3):
        print("Yes")
        exit()

if (np.diag(new_bingo).sum() == 3):
    print("Yes")
    exit()

new_bingo = np.fliplr(new_bingo)

if (np.diag(new_bingo).sum() == 3):
    print("Yes")
    exit()

print("No")
