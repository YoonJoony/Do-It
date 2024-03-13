import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = list(map(str, input().split()))
q = [0 if q[_] == '<' else 1 for _ in range(N)]
v = [0] * 10
MAX = -1
MIN = 10000000000


# 부등호 연산 결과 확인
def inequality_cal(inequality, num1, num2):
    if inequality == 0:
        return num1 < num2
    else:
        return num1 > num2


def dfs(n, lst):
    global MAX, MIN
    if n == N:
        ans = ''.join(str(val) for val in lst)
        if max(int(MAX), int(ans)) == int(ans):
            MAX = ans
        if min(int(MIN), int(ans)) == int(ans):
            MIN = ans
        return

    for i in range(10):  # 0 ~ 9까지 수를 조합
        if v[i] == 0:
            v[i] = 1
            if not lst or inequality_cal(q[n], lst[-1], i):
                dfs(n + 1, lst + [i])
            v[i] = 0


dfs(-1, [])
print(MAX)
print(MIN)