import sys
from collections import deque
import re
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip('\n')
    n = int(input())
    num = deque(re.findall(r'\d+', input().rstrip('\n')))

    reverse_flag = True
    error_flag = True

    for val in p:
        if val == "R":
            if reverse_flag:
                reverse_flag = False
            else:
                reverse_flag = True
        else:
            if not num:
                error_flag = False
                print("error")
                break
            if reverse_flag:
                num.popleft()
            elif not reverse_flag:
                num.pop()
    if not reverse_flag:
        num.reverse()

    if error_flag:
        print('[' + ','.join(num) + ']')
