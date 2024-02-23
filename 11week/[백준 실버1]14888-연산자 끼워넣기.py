from itertools import combinations
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
cal_arr = list(map(int, input().split()))

cal = []
cal_str = ['+', '-', '*', '/']
max_result = -float('inf')
min_result = float('inf')

# 연산자 입력값으로 연산자가 나열된 배열을 만듬.
for i, val in enumerate(cal_arr):
    for _ in range(val):
        cal.append(cal_str[i])


# 연산 함수
# A : 연산자, temp : 계산 결과, i : 더해줄 배열 위치
def calculator(A, temp, i):
    if A == '+':
        return temp + numbers[i]
    elif A == '-':
        return temp - numbers[i]
    elif A == '*':
        return temp * numbers[i]
    elif A == '/':
        if temp < 0:
            temp = abs(temp)
            return (temp // numbers[i]) * -1
        else:
            return temp // numbers[i]


def dfs(n, lst, sum):
    global max_result, min_result
    if n == N - 1:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return

    prev = 0  # '++...' '-*///' 처럼 중복 기호가 있을 시 제외해주기 위해
    for i in range(0, len(cal)):
        if not visited[i] and prev != cal[i]:
            prev = cal[i]
            visited[i] = True
            # 기호 조합을 맞춰가며 동시에 연산도 같이 해준다.
            dfs(n + 1, lst + [cal[i]], calculator(cal[i], sum, n + 1))
            visited[i] = False


visited = [False for _ in range(len(cal))]
dfs(0, [], numbers[0])
print(max_result)
print(min_result)
