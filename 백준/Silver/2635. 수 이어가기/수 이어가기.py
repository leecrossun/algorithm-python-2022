# 수 이어가기
num = int(input())
cnt, answer = 0, [num]

def make_number(n):
    num_list = [num, n]
    idx = 0
    while 1:
        new_num = num_list[idx] - num_list[idx+1]
        if new_num < 0:
            break
        else:
            num_list.append(new_num)

        idx += 1

    return  len(num_list), num_list

# Main
for n in range(1, num+1):
    new_cnt, new_list = make_number(n)
    
    if new_cnt > cnt:
        cnt, answer = new_cnt, new_list

print(cnt)
for ans in answer:
    print(ans, end=' ')