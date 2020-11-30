

s = input()

q = int(input())

#t,f,c = map(str,input().split())

#t = 1  反転

#t = 2 
#   f = 1 => c + s
#   f = 2 => s + c 
front = []
back = []
fb_judge =0 #0の時通常方向
for i in range(q):

    tfc = list(map(str,input().split()))

    if (tfc[0] == "1"):
        fb_judge += 1
        continue

    
    if (tfc[0] == "2"):
        
        if (fb_judge % 2 == 0 and tfc[1] == "1"):
            front.append(tfc[2])
            #s = tfc[2] + s

        elif(fb_judge % 2 == 0 and tfc[1] == "2"):
            back.append(tfc[2])
            #s = s + tfc[2]

        elif(fb_judge % 2 == 1 and tfc[1] == "1"):
            back.append(tfc[2])
            #s = s + tfc[2]

        elif(fb_judge % 2 == 1 and tfc[1] == "2"):
            front.append(tfc[2])
            #s = tfc[2] + s
        
        else:
            pass

#front = []
#back = []

if (fb_judge % 2 == 0):
    print("".join(front[::-1])+ s+ "".join(back))
    #print(s)

else:
    print("".join(back[::-1])+ s[::-1]+ "".join(front))
    #print(s[::-1])
"""
a
9
2 2 a
2 1 b
1
2 2 c
1
1
1
2 2 b
2 1 a


""" 


