def dfs(start):
    global result, cnt
    P = 0
    flag = 0
    while P < N:
        result = arr[P] + arr[:flag]


N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for _ in range(N)]
result = 0
cnt = 0
dfs(0)
print(cnt)