# 팰린드롬수
while 1:
    n = input()
    if n == "0": break
    size = len(n)
    mid = size // 2
    left = n[:mid]

    if size % 2 == 0:
        right = "".join(reversed(n[mid:]))
    else:
        right = "".join(reversed(n[mid + 1:]))

    if left == right:
        print("yes")
    else:
        print("no")