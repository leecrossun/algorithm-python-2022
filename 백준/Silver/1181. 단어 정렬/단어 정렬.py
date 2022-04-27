# 단어 정렬
import heapq
from collections import deque
N = int(input())
heap = []
words = deque([])
for _ in range(N):
    word = input()
    if word not in words:
        heapq.heappush(heap, (len(word), word))
        words.append(word)
for _ in range(len(heap)):
    w = heapq.heappop(heap)
    print(w[1])