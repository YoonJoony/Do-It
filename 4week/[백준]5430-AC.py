import sys
import re
input = sys.stdin.readline

for _ in range(int(input())):
    cal = []
    for val in input().rstrip('\n'):
        cal.append(val)
    N = int(input())
    input_string = input().rstrip('\n')
    arr = [int(num) for num in re.findall(r'\d+', input_string)]
    re_arr = []

    # 여기가 문제? RDRRDRD 일 경우는 계산이 안됨.
    if cal.count('R') % 2 == 1:
        re_arr.extend(reversed(arr))
        arr = re_arr

    D_count = cal.count('D')

    if len(arr) < D_count:
        print("error")
    else:
        result = arr[D_count:]
        print(str(result).replace(" ", ""))




