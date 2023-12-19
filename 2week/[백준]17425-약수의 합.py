import sys

input = sys.stdin.readline
M = int(input())
arr = []
for i in range(M):
    sum = 0

    N = int(input())

    for i in range(1, N+1):
        arr.append(i)

    for i in range(N):
        if arr[i] == 0:
            sum += i

    N -= 1

    print(sum)

# 1
# 1 2
# 1 2 3
#   1 3 6
# 1 2 3 4
#   1 3 6 10
#   1 3 2 2
# 1 2 3 4 5
#    1 3 6 10 15
#    1 3 1