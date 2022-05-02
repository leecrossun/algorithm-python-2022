# 동전2
n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
dp = [10001] * (k+1)
dp[0] = 0

for c in coin:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == 10001: dp[k] = -1
print(dp[k])