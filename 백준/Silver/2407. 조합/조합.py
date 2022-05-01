# 조합
N, M = map(int, input().split())

n1 = 1
for i in range(M):
    n1 *= N-i 

n2 = 1
for i in range(1, M+1):
    n2 *= i

answer = n1 // n2
print(answer)