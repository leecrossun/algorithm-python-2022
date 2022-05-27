# DFS와 BFS
from collections import deque
N, M, V = map(int, input().split())
g = [[] for _ in range(N+1)]

def bfs(s):
    visited = [False] * (N + 1)
    visited[s] = True
    q = deque([s])
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in g[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

visited = [False] * (N + 1)
def dfs(s):
    visited[s] = True
    print(s, end=' ')
    for i in g[s]:
        if not visited[i]:
            dfs(i)

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, N+1):
    g[i].sort()

dfs(V)
print("")
bfs(V)