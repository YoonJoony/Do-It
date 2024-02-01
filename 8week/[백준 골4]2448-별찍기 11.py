
add_stars = 1

star = '*'


def star_eleven(x, y, size, add_star):
    global star
    graph[x][y] = star

    if size == 1:
        return

    for i in range(size):
        for j in range(size):
            new_size = size // 2
            for k in range(3):
                for l in range(k + add_star):
                    star_eleven(x + k, l, new_size, add_star)
                add_star += 1
            return


# def star_eleven(n):
#     global k
#     for i in range(1, n+ 1):
#         for l in range(n - i):
#             print(" ", end="")
#         for j in range(i + k):
#             print("*", end="")
#         k += 1
#         print()

n = int(input())
graph = [[" " for _ in range(n*2-1)] for _ in range(n)]
star_eleven(0, 0, n, add_stars)

for i in range(n):
    for j in range(n*2-1):
        print(graph[i][j], end="")
    print()