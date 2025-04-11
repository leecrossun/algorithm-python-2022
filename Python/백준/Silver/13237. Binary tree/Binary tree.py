# 13237 Binary tree
from collections import deque
N = int(input())
tree = {k: [] for k in range(1, N+1)}
level = [0]*(N+1)
root = 0

for i in range(1, N+1):
    node = int(input())
    if(node == -1): root = i
    else:
        tree[node].append(i)

level[root] = 0
current_lv = 0

q = deque([(root, 0)])
while q:
    node, lv = q.popleft()
    children = tree[node]
    for child in children:
        level[child] = lv+1
        q.append((child, lv+1))

for i in range(1, len(level)): print(level[i])

