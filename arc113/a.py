
k = int(input())
cnt = 0
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append([i,n//i])
            
            if i != n // i:
                divisors.append([n//i,i])


    divisors.sort()
    return divisors

def num_divisors_table(n):
    table = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1
    
    return table

"""
yakusu_lst = []
yakusu_lst.append(0)
for i in range(1,2*(10**5)+1):
    yakusu_lst.append(len(make_divisors(i)))
"""

#print(num_divisors_table(2*100000))
yakusu_lst = num_divisors_table(2*(10**5)+1)
#print(yakusu_lst[:15])
for i in range(1,k+1):
    #print(make_divisors(i))

    for l in make_divisors(i):
        #print(l,l[0])
        cnt += yakusu_lst[l[0]]
    #a = make_divisors(i)

print(cnt)

