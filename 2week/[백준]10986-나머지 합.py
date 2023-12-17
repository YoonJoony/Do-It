import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
D = [0] * N
C = [0] * M
count = 0

D[0] = A[0]

for i in range(1, N):
    D[i] = D[i-1] + A[i]

for i in range(N):
    re = D[i] % M
    if re == 0:
        count += 1
    C[re] += 1

for i in range(M):
    if C[i] > 1:
        count += (C[i] * (C[i]-1) // 2)


print(count)