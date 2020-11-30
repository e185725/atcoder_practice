
n = int(input())

result = {"AC" : 0,"WA":0,"TLE":0,"RE":0}

for i in range(n):
    judge = input()
    result[judge] += 1

for i in result:
    print(i ,"x",result[i])
