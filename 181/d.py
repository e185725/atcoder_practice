from collections import Counter
#二桁以内の4の倍数の配列
n_4 = [ 4 * i for i in range(3,250)]
#print(n_4)
S = list(input())
#print(S)
num_dict = {str(i):0 for i in range(10)} 
for i in S:
    num_dict[str(i)] += 1 
if (len(S) <= 2 and ( int("".join(S)) % 8 == 0 or int("".join(reversed(S))) % 8== 0 )):
    print("Yes")
    exit()
for i in range(104,1000,8):#3桁の八の倍数を出力していく
    test_num_dict = {str(i):0 for i in range(10)} 
    count = 0
    num = list(str(i))
    for l in num:
        test_num_dict[l] += 1
    for l in range(10):
        if(num_dict[str(l)] - test_num_dict[str(l)] < 0):
            count += 1
    if(count == 0):
        print("Yes")
        exit()
print("No")
    


    




