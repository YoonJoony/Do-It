def dfs(start):
    global result, cnt
    P = 0
    flag = P + 1
    while P < N:
        if flag >= N:
            P += 1
            flag = P + 1
        if P == N:
            return
        if arr[P] == S:
            cnt += 1

        result = arr[P]
        for i in range(flag, N):
            result = result + arr[i]
            if result == S:
                cnt += 1

        flag += 1
        result = 0


N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for _ in range(N)]
result = 0
cnt = 0
dfs(0)
print(cnt)
