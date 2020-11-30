n = input()

a = 0
for i in range(len(n)):
    a += int(n[i])



if (a % 9 == 0):
    print("Yes")
else:
    print("No")