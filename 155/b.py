

n = int(input())

a = list(map(int,input().split()))
count =0
count_2 = 0
for i in a:
    if (i % 2 == 0):
        count += 1

        if (i % 3 == 0 or i % 5 == 0):
            count_2 += 1



if (count == count_2):
    print("APPROVED")

else:
    print("DENIED")