for _ in range(int(input())):
    n = int(input())
    sm = [1, 2, 3]
    cnt = 0

    def dfs(lst):
        global cnt
        if sum(lst) == n:
            cnt += 1
            return

        for i in range(3):
            if sum(lst) + sm[i] <= n:
                dfs(lst + [sm[i]])


    dfs([])
    print(cnt)