import sys
input = sys.stdin.readline

N, K = map(int, input().split())

array = []
array_sum = 0

for i in range(N):
    array.append(list(map(int, input().split())))

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x2-x1+1):
        for k in range(y1-1, y2):
            array_sum += array[x1-1+j][k]

    print(array_sum)
    array_sum = 0