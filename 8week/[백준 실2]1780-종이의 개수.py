import sys
input = sys.stdin.readline


def check_paper(x, y, size):
    global minus_one, one, zero
    # 종이가 모두 같은 수로 되어 있다면 종이를 그대로 사용
    # 아닌 경우.. => 입력 받은 배열을 전부 돌며 모두 같은지 확인
    visited = graph[x][y]  # 처음 선택한 배열
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != visited:  # 배열이 모두 같지 않을경우
                new_size = size // 3
                for k in range(3):
                    for j in range(3):
                        check_paper(x + k * new_size, y + j * new_size, new_size)
                        # 해당 매개변수 안에 x + / y + 를 해준 이유
                        # check_paper(?, ?, 3). 즉, 배열이 3x3이 될 때 크기가 모두 같지 않을 경우 다를 경우
                        # check_paper(?, ?, 1)로 재귀된다.
                        # 근데 각 매개변수 ?, ? 에 x, y를 더하지 않았을 경우
                        # 3x3 배열 위치가 어디든 check_paper(?, ?, 1)재귀 시 0, 0부터 탐색되게 된다.
                return
    if visited == -1:
        minus_one += 1
    elif visited == 1:
        one += 1
    else:
        zero += 1


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
minus_one, one, zero = 0, 0, 0
check_paper(0, 0, n)

print(minus_one, one, zero)