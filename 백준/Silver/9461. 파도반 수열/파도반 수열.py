# 파도반 수열 - 다이나믹 프로그래밍
def fn(n):
    dp = [0, 1, 1, 1, 2] + [0] * (n-4)
    if n < 5:
        return dp[n]
    for i in range(5, n+1):
        dp[i] = dp[i-5] + dp[i-1]
    return dp[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(fn(N))