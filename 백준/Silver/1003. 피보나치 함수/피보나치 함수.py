# 피보나치 함수
T = int(input())
for _ in range(T):
    N = int(input())
    cnt_zero = 0
    cnt_one = 0

    memo = list([0, 0] for _ in range(N+1))
    memo[0] = [1, 0]
    if N > 0:
        memo[1] = [0, 1]

    for i in range(2, N+1):
        fibo_1 = memo[i-1]
        fibo_2 = memo[i-2]
        memo[i] = [fibo_1[0] + fibo_2[0], fibo_1[1] + fibo_2[1]]

    print(memo[N][0], memo[N][1])