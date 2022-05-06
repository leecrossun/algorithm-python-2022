# 촌수계산
from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = list([False] * (n+1) for _ in range(n+1))
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent][child] = True
    graph[child][parent] = True

visited = [0] * (n + 1)
q = deque([a])

while q:
    v = q.pop()
    for idx in range(n+1):
        if visited[idx] == 0 and graph[v][idx] == True:
            q.append(idx)
            visited[idx] = visited[v] + 1
            if idx == b:
                break
                
if visited[b] == 0: 
    print("-1")
else: 
    print(visited[b])