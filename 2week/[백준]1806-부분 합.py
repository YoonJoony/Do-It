import sys
input = sys.stdin.readline

N, S = map(int, input().split())

A = list(map(int, input().split()))
end = 0
count = []
sum = 0
for i in range(N):
    while sum < S and end < N:
        sum += A[end]
        end += 1
    if sum >= S:
        # for j in range(i, end):
        #     print(f"{A[j]}", end=" ")
        # print()
        count.append(end-i)
    sum -= A[i]
print(count)




