# 방 배정
import math
N, K = map(int, input().split()) # 학생 수, 최대 인원 수
stu = list(list(map(int, input().split())) for _ in range(N)) # 성별, 학년

# stu_class[학년][성별 여 0 남 1]
stu_class = list([0, 0] for _ in range(6))
for s in stu:
    gender, grade = s[0], s[1]
    stu_class[grade-1][gender] += 1

room = 0
for count in stu_class:
    girl =  math.ceil(count[0] / K) if count[0] != 0 else 0
    boy = math.ceil(count[1] / K) if count[1] != 0 else 0
    room += girl + boy
print(room)