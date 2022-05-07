# 최단경로
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

# n : 노드의 수 / m : 간선의 수
n, m = map(int, input().split())

# start : 시작노드
start = int(input())

# 노드정보
graph = [[] for _ in range(n+1)]

# 방문정보
visited = [False] * (n+1)

# 최단 거리 테이블 (무한으로 초기화)
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a -> b (비용 c)
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, v = heapq.heappop(q) # 최단거리가 가장 짧은 노드 반환
        if distance[v] < dist: # 현재 노드가 이미 처리되었으면
            continue # 건너뛰기
        for i in graph[v]: # 현재 노드와 연결된 노드 확인
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거치는 게 더 빠를 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])