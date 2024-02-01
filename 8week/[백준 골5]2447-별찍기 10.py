import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def star_ten(x, y, size, star):
    count = 0
    graph[x][y] = star

    if size == 1:
        return

    for i in range(x, x + size):
        for j in range(y, y + size):
                new_size = size // 3
                for k in range(3):
                    for l in range(3):
                        count += 1
                        mx = x + k * new_size
                        my = y + l * new_size
                        if count == 5:
                            continue
                        else:
                            star_ten(mx, my, new_size, '*')
                return


n = int(input())
graph = [[" " for _ in range(n)] for _ in range(n)]
star_ten(0, 0, n, '*')
for i in range(n):
    for j in range(n):
        print(graph[i][j], end="")
    print()
