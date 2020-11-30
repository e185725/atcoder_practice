"""
#n = 1000000000000001
#n = 123456789
n = int(input())
#n = 27
# 1000000000000001
# 205891132094649　27の10乗
# 5559060566555523　27の11乗

#このことから　文字列は最大でも11文字である。

eng = list(" abcdefghijklmnopqrstuvwxyz")
ans = []
a = 26
count = 0
while (n  > a**count ):
    count += 1
    #print(count)
#print(a**11)
#count -= 1
#print(n)
for i in range(count,0,-1):
    #print(n // a)
    #print(n % a)
    ans.append(n % a)
    n = n//a

#print(ans)
ans_last = ""
if (ans == []):
    ans_last += "a"
    #exit()
for i in range(len(ans)):


    ans_last += eng[ans[i]]
  
    
print(ans_last[::-1])
"""
def nummm(n):
  if n <= 26:
    return chr(96 + n)
  elif n%26 == 0:
    return nummm(n//26 - 1) + chr(122)
  else:
    return nummm(n//26) + chr(n%26 + 96)

s = int(input())
print(nummm(s))
