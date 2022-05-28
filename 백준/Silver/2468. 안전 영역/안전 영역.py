# 안전 영역 - BFS
from collections import deque
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

max_h, min_h = 0, 100
for a in area:
    max_h = max(max(a), max_h)
    min_h = min(min(a), min_h)

mr = [0, -1, 0, 1]
mc = [1, 0, -1, 0]
def bfs(start_r, start_c):
    global visited, r, c
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    while q:
        vr, vc = q.popleft()
        for i in range(4):
            mv_r = vr + mr[i]
            mv_c = vc + mc[i]
            if 0 <= mv_r < N and 0 <= mv_c < N and not visited[mv_r][mv_c] and area[mv_r][mv_c] > h:
                q.append((mv_r, mv_c))
                visited[mv_r][mv_c] = True


ans = 1
for h in range(min_h, max_h):
    visited = [[False] * N for _ in range(N)]
    safe_sec = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and area[r][c] > h:
                bfs(r, c)
                safe_sec += 1
    ans = max(ans, safe_sec)
print(ans)