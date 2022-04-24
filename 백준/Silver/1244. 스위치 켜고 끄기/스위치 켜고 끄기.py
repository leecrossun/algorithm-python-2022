# 스위치 켜고 끄기
switch_cnt = int(input()) # 스위치 개수
switch_state = list(map(int, input().split())) # 스위치 상태
student_cnt = int(input()) # 학생수

def boy_control(num):
    for i in range(switch_cnt):
        if (i+1) % num == 0:
            switch_state[i] = 0 if switch_state[i] == 1 else 1


def girl_control(num):
    num -= 1
    switch_state[num] = 0 if switch_state[num] == 1 else 1

    i, j = num-1, num+1
    while 1:
        if i < 0 or j >= switch_cnt or switch_state[i] != switch_state[j]:
            break
        
        switch_state[i] = 0 if switch_state[i] == 1 else 1
        switch_state[j] = 0 if switch_state[j] == 1 else 1

        i -= 1
        j += 1

# Main
for _ in range(student_cnt):
    gender, num = map(int, input().split())
    boy_control(num) if gender == 1 else girl_control(num)

div = 20
for idx in range(0, switch_cnt + div - 1, div):
    print_list = switch_state[idx:idx + div] if idx + div <= switch_cnt else switch_state[idx:]
    if print_list != []:
        for p in print_list:
            print(p, end=' ')
        print("")