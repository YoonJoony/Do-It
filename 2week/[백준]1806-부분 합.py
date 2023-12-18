import sys
input = sys.stdin.readline

N, S = map(int, input().split())

A = list(map(int, input().split()))
end = 0
sum = 0
count = 0
for i in range(N):
    while sum < S and end < N:
        sum += A[end]
        end += 1
    if sum >= S:
        if count == 0:
            count = end-i
        else:
            count = min(count, (end-i))
    sum -= A[i]

print(count)


