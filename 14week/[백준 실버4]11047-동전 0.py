import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input().strip('\n')) for _ in range(N)]
cnt = 0
for i in range((N-1), -1, -1):
    if K // A[i]:
        cnt += K // A[i]
        K %= A[i]

    if K == 0:
        break

print(cnt)