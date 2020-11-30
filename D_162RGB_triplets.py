#N = int(input())
#S = list(input())
N = 39
S = list("RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB")
#print(S)

RGB = []
R = []
G = []
B = []
for i in range(N):
    if(S[i] == "R"):
        R.append(i)
    elif(S[i] == "G"):
        G.append(i)
    else:
        B.append(i)

RGB.append(R)
RGB.append(G)
RGB.append(B)
print(RGB)
a = len(R)*len(G)*len(B)
ans = 0
for r in R:
    for g in G:
        for b in B:
            if( r+b == 2*g):
                print(r,g,b)
                continue

            ans += 1

print(ans,a)
