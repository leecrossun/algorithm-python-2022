# 줄세우기
N = int(input())
stu = list(map(int, input().split()))
answer = []
num = 1
for s in stu:
    size = len(answer)
    answer.insert(size-s, num)
    num += 1
for a in answer:
    print(a, end=' ')