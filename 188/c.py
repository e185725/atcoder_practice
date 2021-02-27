n = int(input())


a = list(map(int,input().split()))
last_ans = a.copy()
while (True) :
    ans = []

    if (len(a) == 2):
        print(last_ans.index(min(a))+1)
        break
    for i in range(0,len(a),2):
        if (a[i] > a[i+1]):
            ans.append(a[i])
        else:
            ans.append(a[i+1])
    a = [i for i in ans]
    #print(a)

        
