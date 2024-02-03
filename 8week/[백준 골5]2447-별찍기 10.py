import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def star_ten(size):
    new_size = size // 3
    if size == 3: # 3x3 크기 원본 배열 설정
        graph[1] = ['*', ' ', '*']
        graph[0][:3] = graph[2][:3] = ['*'] * 3
        return

    star_ten(new_size)

    for i in range(0, size, new_size): # i, ㅓ 에 new_size를 더하면서 반복
        for j in range(0, size, new_size):
            if i != new_size or j != new_size:
                for k in range(new_size):
                    # new_ize 크기 만큼 원본배열 복사
                    graph[i+k][j:j+new_size] = graph[k][:new_size]
                    # new_size만큼 복사


n = int(input())
graph = [[" " for _ in range(n)] for _ in range(n)]

star_ten(n)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end="")
    print()
