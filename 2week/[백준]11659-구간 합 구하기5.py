import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
S = 0
for i in range(M):
    num1, num2 = map(int, input().split())

    for i in range((num2-num1)+1):
        S += A[i+(num1-1)]

    print(S)
    S = 0

# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# A = list(map(int, input().split()))
# D = [0] * (N+1)
#
# for i in range(1, N+1):
#     D[i] = D[i-1] + A[i-1]
#
# for i in range(M):
#     num1, num2 = map(int, input().split())
#     S = D[num2] - D[num1-1]
#     print(S)

