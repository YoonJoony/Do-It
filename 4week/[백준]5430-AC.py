import sys
import re
input = sys.stdin.readline

for _ in range(int(input())):
    p = input()
    n = int(input())
    num = re.findall(r'\d+', input().rstrip('\n'))

    for val in p:
        if val == "R":
            num.reverse()
        elif val == "D":
            if not num:
                num = "error"
                break
            else:
                num.remove(num[0])
    if num != "error":
        print("[", end="")
        print(",".join(num), end="")
        print("]")
    else:
        print(num)



# 100 x 100000