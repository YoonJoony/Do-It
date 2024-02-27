import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(n, arr, cnt): # n : 손에 든 계란 위치 // arr : 계란 정보 // cnt : 깨진 계란 개수
    global result
    if n == N:  # 손에 든 계란이 맨 오른쪽인 경우
        result = max(result, cnt)
        return

    S, W = arr[n]  # 손에 든 계란 무게, 내구도

    if S <= 0:  # 손에 든 계란이 깨진거면 리턴
        dfs(n + 1, arr, cnt)
        return

    for i in range(0, N):
        if arr[i][0] > 0 and i != n: # 칠 계란이 안깨져있을 경우
            next_S, next_W = arr[i]  # 칠 계란의 무게, 내구도

            arr[n][0] = S - next_W  # 치고 난 후 계란 정보 업데이트
            arr[i][0] = next_S - W

            cnt_temp = 0 # 두 계란 깨진 여부 변수

            if arr[n][0] <= 0 and arr[i][0] <= 0:
                cnt_temp = 2  # 업데이트 된 계란 정보 넘겨줌
            elif arr[n][0] <= 0 or arr[i][0] <= 0:
                cnt_temp = 1  # 업데이트 된 계란 정보 넘겨줌

            dfs(n + 1, arr, cnt + cnt_temp)

            arr[n][0] = S  # 치고 난 후 계란 다시 수정
            arr[i][0] = next_S

    result = max(result, cnt) # 더이상 칠 계란이 없을 경우 여태 쳤던 깨진 계란 수 업데이트

lst = []
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))
N = len(lst)
result = 0 # max로 깨진 계란
dfs(0, lst, 0)
print(result)
