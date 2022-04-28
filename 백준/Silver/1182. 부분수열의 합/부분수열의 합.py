# 부분수열의 합
from itertools import combinations
N, S = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(1, len(numbers)+1):
    combination = combinations(numbers, i)
    for c in combination:
        if sum(c) == S:
            cnt += 1
print(cnt)