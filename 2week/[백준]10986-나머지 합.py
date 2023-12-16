import sys

input = sys.stdin.readline

N, M = map(int, input().split())

loop_N = N

A = list(map(int, input().split()))
flag = 0
count = 0
i = 1
D = [0 for _ in range(N + 1)]

while flag < loop_N:
    D[i] = D[i - 1] + A[i + flag - 1]

    if D[i] % M == 0:
        print(D[i])
        count += 1

    if i == N:
        flag += 1
        i = 1
        N -= 1
        D = [0 for _ in range(N + 1)]
    else:
        i += 1

print(count)




