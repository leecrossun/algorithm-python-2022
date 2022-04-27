# 좌표 정렬하기 2
import heapq
N = int(input())
heap = []
for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(heap, (y, x))
for _ in range(N):
    v = heapq.heappop(heap)
    print(v[1], v[0])