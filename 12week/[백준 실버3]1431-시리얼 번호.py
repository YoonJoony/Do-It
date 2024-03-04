import re
from functools import reduce
# 1. 길이가 짧을 경우
# 2. 숫자의 합이 작을 경우
# 3. 사전순으로 작을 경우


def sum_of_num(s):
    # 시리얼 번호 s의 모든 숫자의 합
    return sum(int(char) for char in s if char.isdigit())


N = int(input())
lst = [input().strip() for _ in range(N)]

# (len(x), sum_of_num(x), x) : 위 순서에 맞게 정렬 조건을 만족시켜줌.
# 1순위 len(x)
# 2순위 숫자 합
# 3순위 x, 즉 사전순
sort_num = sorted(lst, key=lambda x: (len(x), sum_of_num(x), x))


for val in sort_num:
    print(val)