# 스티커 - 다이나믹 프로그래밍
def fn(n):
    s = [[0] + list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (n+1) for _ in range(2)]
    dp[0][0] = dp[1][0] = 0
    dp[0][1], dp[1][1] = s[0][1], s[1][1]
    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + s[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + s[1][i]
    return max(dp[0][n], dp[1][n])

T = int(input())
for _ in range(T):
    N = int(input())
    print(fn(N))