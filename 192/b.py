
s = input()

a = "abcdefghijklmnopqrstuvwxyz"
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i,l in enumerate(s):
    #print(i+1,l)
    if ( (i+1) % 2 == 1 and (l in a)):
        continue

    if ( (i+1) % 2 == 0 and (l in A)):
        continue

    #print(l)
    print("No")
    exit()

print("Yes")

