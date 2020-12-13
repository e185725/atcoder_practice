
n = int(input())

t = input()


s = "110"*(2*10**5)
s_1 = s[1:]+"1"
s_2 = s[2:]+"11"
count = 0
if (t in s[:n]):
    count += 100
if (t in s_1[:n]):
    count += 10
if (t in s_2[:n]):
    count += 1


if (count >= 100 and n == 3):
    print(3*(10**10)//3 )

elif (count > 0 and n == 3):
    print(3*(10**10)//3 - n//3)

elif (count > 0 and n > 2):
    print(3*(10**10)//3 - n//3)

elif(count >= 10 and n == 2):
    print(3*(10**10)//3 - n//3)

elif(count > 0 and n == 2):
    print(3*(10**10)//3 - n//3 -1)

elif (count > 0 and t == "0"):
    print(10**10)
elif (count > 0 and t == "1"):
    print(2*10**10)
else :
    print(0)