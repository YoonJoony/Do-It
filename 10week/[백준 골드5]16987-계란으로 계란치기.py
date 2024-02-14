# 4개 이상시 우선순위
# 1. 둘 다 깨져야함
# 2. 하나만 깨져야함

# 3개 이하시 하나만 깨져야함.
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(n, arr, cnt):
    global result
    if n == N:  # 손에 든 계란이 맨 오른쪽인 경우
        result = max(result, cnt)
        return

    S, W = arr[n]  # 손에 든 계란 무게, 내구도

    if S <= 0:  # 손에 든 계란이 깨진거면 리턴
        dfs(n + 1, arr, cnt)
        return

    for i in range(0, N):  # N개 중 2개를 고를 수 있는 모든 경우 수를 찾아야함
        if arr[i][0] > 0 and i != n:
            next_S, next_W = arr[i]  # 칠 계란의 무게, 내구도

            cal_S = S - next_W
            cal_next_S = next_S - W

            arr[n][0] = cal_S  # 치고 난 후 계란 정보 업데이트
            arr[i][0] = cal_next_S

            cnt_temp = 0

            if cal_S <= 0 and cal_next_S <= 0:
                cnt_temp = 2  # 업데이트 된 계란 정보 넘겨줌
            elif cal_S <= 0 or cal_next_S <= 0:
                cnt_temp = 1  # 업데이트 된 계란 정보 넘겨줌

            dfs(n + 1, arr, cnt + cnt_temp)

            arr[n][0] = S  # 치고 난 후 계란 다시 수정
            arr[i][0] = next_S

    result = max(result, cnt) # 더이상 칠 계란이 없을 경우 여태 쳤던 깨진 계란 수 업데이트


lst = []
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))
N = len(lst)
result = 0
dfs(0, lst, 0)
print(result)
