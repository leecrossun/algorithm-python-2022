# 가로수
def get_common_factor(a, b):
    while 1:
        r = a % b
        if r == 0:
            return b
        a, b = b, r

# Main
N = int(input())
num = []
gap = []

for _ in range(N):
    num.append(int(input()))

for i in range(N-1):
    gap.append(num[i+1] - num[i])

c_factor = gap[0] # 최대공약수
for g in gap:
    c_factor = get_common_factor(c_factor, g)

count = 0
for g in gap:
    count += (g // c_factor - 1)
print(count)