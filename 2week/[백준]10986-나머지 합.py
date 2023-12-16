N, M = map(int, input().split())

loop_N = N

A = list(map(int, input().split()))
flag = 0
count = 0
while flag < loop_N:
    D = [0 for _ in range(N+1)]

    for i in range(1, len(D)):
        D[i] = D[i-1] + A[i+flag-1]

        if D[i] % M == 0:
            count += 1

    N -= 1
    flag += 1

print(count)
