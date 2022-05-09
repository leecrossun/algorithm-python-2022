# 점프 - 다이나믹 프로그래밍
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

def fn(x, y):
    if x == 0 and y == 0:
        dp[x][y] = 1
        return
    down = 0
    for i in range(x): down += dp[i][y] if board[i][y] == x - i else 0

    right = 0
    for i in range(y): right += dp[x][i] if board[x][i] == y - i else 0

    dp[x][y] = down + right
    return

for i in range(N):
    for j in range(N):
        fn(i, j)

print(dp[N-1][N-1])