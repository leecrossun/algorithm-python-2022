# 홀수
num = [int(input()) for _ in range(7)]
arr = []
for n in num:
    if n % 2 != 0:
        arr.append(n)
if len(arr) == 0:
    print("-1")
else:
    print(sum(arr))
    print(min(arr))