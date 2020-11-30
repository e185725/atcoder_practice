
import collections
n = int(input())

a_lst = list(map(int,input().split()))

a_counter = collections.Counter(a_lst)

#print(a_counter)

ans = 0
for i in a_counter.values():
    ans += i * (i - 1) //2


#print(ans)

for i in a_lst :
    ans_a = ans
    ans_a -= (a_counter[i]) * (a_counter[i]-1) // 2
    ans_a += (a_counter[i] -1) * (a_counter[i]-2) // 2

    print(ans_a)