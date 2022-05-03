# 연속합
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0], ans = arr[0], arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    ans = max(ans, dp[i])

print(ans)