import sys
input = sys.stdin.readline


def color_paper(x, y, size):
    global white, blue
    visited = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != visited:
                new_size = size // 2
                for k in range(2):
                    for l in range(2):
                        color_paper(x + k * new_size, y + l * new_size, new_size)
                return

    if visited == 0:
        white += 1
    else:
        blue += 1


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
color_paper(0, 0, n)

print(white)
print(blue)