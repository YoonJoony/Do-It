import sys
from itertools import combinations

N = int(input())


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


for _ in range(N):
    l = list(map(int, sys.stdin.readline().split()[1:]))
    ans = 0
    for i in list(combinations(l, 2)):
        ans += gcd(*i)
    print(ans)

# import sys
# from math import gcd
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
#
# for _ in range(int(input())):
#     N, *arr = list(map(int, input().split()))
#     sorted(arr)
#     result = 0
#
#
#     def dfs(n, lst, start):
#         global result
#         if n == 2:
#             result += gcd(lst[0], lst[1])
#             return
#         for i in range(start, N):
#             dfs(n+1, lst + [arr[i]], i+1)
#
#
#     dfs(0, [], 0)
#
#     print(result)