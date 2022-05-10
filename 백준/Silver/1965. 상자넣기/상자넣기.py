# 상자넣기 - 다이나믹 프로그래밍
N = int(input())
box = list(map(int, input().split()))
dp = [1] * N
for i in range(1, N):
    small_box = []
    for j in range(0, i):
        if box[j] < box[i]:
            small_box.append(dp[j])
    if small_box: dp[i] = max(small_box) + 1
print(max(dp))