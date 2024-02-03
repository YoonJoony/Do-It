import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def star_ten(x, y, size):
    if size == 1:
        graph[x][y] = '*'
        return

    new_size = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            star_ten(x + i * new_size, y + j * new_size, new_size)


n = int(input())
graph = [[" " for _ in range(n)] for _ in range(n)]

star_ten(0, 0, n)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end="")
    print()
