
from collections import deque

H,W = map(int,input().split())

S = [input() for _ in range(H)]

def bfs(si,sj):

    dist = [ [-1]*W for _ in range(H)]
    #0は通過を表す
    q = deque([(si,sj)])
    dist[si][sj] = 0

    while q:
        i,j = q.popleft()
        
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:

            newi,newj = i+di,j+dj

            if newi < 0 or H <= newi:
                continue

            if newj < 0 or W <= newj:
                continue

            if S[newi][newj] == "#":
                continue

            if dist[newi][newj] > -1:
                continue

            dist[newi][newj] = dist[i][j] + 1
            q.append( (newi,newj))

    return max(sum(dist,[]))

ans = max(bfs(i,j) for i in range(H) for j in range(W) if S[i][j]==".")
print(ans)
           