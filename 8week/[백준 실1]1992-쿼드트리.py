import sys

input = sys.stdin.readline


def querdTree(x, y, size):
    visited = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != visited:
                new_size = size // 2
                print("(", end="")
                for k in range(2):
                    for l in range(2):
                        querdTree(x + k * new_size, y + l * new_size, new_size)
                print(")", end="")
                return
    print(visited, end="")


n = int(input())
graph = [list(input().rstrip('\n')) for _ in range(n)]
querdTree(0, 0, n)
