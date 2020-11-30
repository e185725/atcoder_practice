
a,b,x,y = map(int,input().split())
ans = 0


cost_dp = [0] * (abs(a-b) + 1)

current_area = "A"

#動き方　
 
# a_i <->b_i x+


# a_i+1 <-> b_i  x+

# a_i+1 <-> a_i y+

# b_i+i <-> b_i y+

if (a > b):
    if (a-b == 1):
        ans += x
        print(ans)
        exit()

    if (2*x < y):
        ans += 2*x * (a-b-1)
        ans += x
    
    else:
        ans += y * (a - b -1 )
        ans += x



elif (b > a):
    if (2*x < y):
        ans += 2*x * ( b - a - 1)
        if (2*x > y):

            ans += x + y

        else :
            ans += 3*x

    
    else :
        ans += y * ( b - a )
        ans += x

else :
    ans += x

print(ans)










