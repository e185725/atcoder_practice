
n,k = map(int,input().split())


div = n // k

ans_p = n - div * k

ans_m = abs (ans_p - k)

if (ans_p > ans_m):
    print(ans_m)

else:
    print(ans_p)



