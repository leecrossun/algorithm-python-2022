# 좌표 정렬하기
import heapq
N = int(input())
heap = []
for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(heap, (x, y))
for _ in range(N):
    v = heapq.heappop(heap)
    print(v[0], v[1])