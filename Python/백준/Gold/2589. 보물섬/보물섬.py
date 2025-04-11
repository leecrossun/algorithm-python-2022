# 2589 보물섬
from collections import deque
    
H, W = map(int, input().split())
M = [list(map(str, input())) for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(start_x, start_y):
    length = 0
    
    visited = [[False]*W for _ in range(H)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True

    while q:
        x, y, l = q.popleft()
        length = max(length, l)
        
        for i in range(4):
            mvx, mvy = dx[i], dy[i]
            nx, ny = x + mvx, y + mvy
            if(nx >= 0 and ny >= 0 and nx < H and ny < W):
                if(not visited[nx][ny] and M[nx][ny] == 'L'):
                    q.append([nx, ny, l+1])
                    visited[nx][ny] = True
    return length
        
answer = 0
for i in range(H):
    for j in range(W):
        if(M[i][j] == 'L'):
            answer = max(bfs(i, j), answer)
            
print(answer)