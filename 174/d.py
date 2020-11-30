
N = int(input())

c = input()
count = 0
ans = 0
for i in c :
    if (i == "R"):
        count += 1

for i in range(count):
    if(c[i] == "W"):
        ans += 1

print(ans)
