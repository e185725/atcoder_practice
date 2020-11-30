n = int(input())
a = list(map(int,input().split()))

now = 0
move = 0
move_plus = 0
ans = 0

for ai in a:
    move += ai
    if move>move_plus:
        move_plus = move
        #0地点からのmax距離
        
    ans = max(ans, now+move_plus)
    now += move
    #現在地
    
print(ans)