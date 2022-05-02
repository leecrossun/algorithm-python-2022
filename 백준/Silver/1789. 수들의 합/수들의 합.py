S = int(input())
total, cnt = 0, 0
for i in range(1, S+1):
    total += i
    if total > S: break
    else: cnt += 1
print(cnt)