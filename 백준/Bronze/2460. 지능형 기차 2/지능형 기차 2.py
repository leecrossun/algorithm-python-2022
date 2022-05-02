# 지능형 기차2
answer, current = 0, 0
for _ in range(10):
    get_off, get_on = map(int, input().split())
    current = current - get_off + get_on
    answer = max(answer, current)
print(answer)