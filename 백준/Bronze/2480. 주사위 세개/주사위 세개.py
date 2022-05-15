# 주사위 세개
a, b, c = map(int, input().split())
if a == b == c: ans = 10000 + a * 1000
elif a == b or a == c: ans = 1000 + a * 100
elif b == c: ans = 1000 + b * 100
else: ans = max(a, b, c) * 100
print(ans)