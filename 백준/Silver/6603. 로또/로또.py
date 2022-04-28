# 로또
from itertools import combinations
while 1:
    num = input()
    if num == "0": break
    S = list(map(str, num.split()))[1:]
    s = combinations(S, 6)
    for numbers in s:
        for n in numbers:
            print(n, end = " ")
        print("")
    print("")