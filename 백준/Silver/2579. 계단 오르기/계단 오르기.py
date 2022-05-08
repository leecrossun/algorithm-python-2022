# 계단 오르기 - 다이나믹 프로그래밍
N = int(input())
s = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)
dp[0], dp[1] = 0, s[1]
if N > 1: dp[2] = s[1]+s[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])
print(dp[N])