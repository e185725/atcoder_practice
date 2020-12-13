import math

n = int(input())

t = input()


s = "110"*2*10**5
s_1 = s[1:]+"1" #101
s_2 = s[2:]+"11"#011
count = 0
"""
print(s)
print(s_1)
print(s_2)
"""
if (t in s[:n]):
    count += 100
if (t in s_1[:n]):
    count += 10
if (t in s_2[:n]):
    count += 1

if (t == "1"):
    print(2*10**10)

elif(t == "0"):
    print(10**10)

elif(t == "11" or t == "10"):
    print(10**10)

elif(t == "01"):
    print(10 ** 10 - 1)

elif(t == "110"):
    print(10**10)

elif(t == "011" or t == "101"):
    print(10**10 - 1)

elif (count >= 100 and n % 3 == 0):
    print(10 ** 10 - n//3 + 1)

elif (count >= 100 and n % 3 != 0):
    print(10 ** 10 - n//3 )

elif (count >= 10 and n % 3 == 2):
    print(10 ** 10 - n//3 + 1 )

elif (count >= 10 and n % 3 != 2):
    print(10 ** 10 - n//3 )

elif (count > 0 and n % 3 == 1):
    print(10 ** 10 - n//3 )

elif (count > 0 and n % 3 != 1):
    print(10 ** 10 - n//3 - 1)

else:
    print(0)

