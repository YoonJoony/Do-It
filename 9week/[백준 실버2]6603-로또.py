def dfs(n, start):
    if n == 6:
        print(*result)
        return

    for i in range(start, N + 1):
        result.append(lst[i])
        dfs(n+1, i+1)
        result.pop()

lst = [1]
while lst[0] != 0:
    lst = list(map(int, input().split()))
    N = lst[0]
    result = []
    dfs(0, 1)
    print()
