import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

D = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i-1][j-1]

for i in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())

    result = D[X2][Y2] - D[X1-1][Y2] - D[X2][Y1-1] + D[X1-1][Y1-1]
    print(result)
