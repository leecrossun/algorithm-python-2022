# 수 정렬하기3
import sys
N = int(input())
cnt = [0] * 10001
for _ in range(N):
    n = int(sys.stdin.readline())
    cnt[n] += 1
for i in range(1, 10001):
    for _ in range(cnt[i]):
        print(i)