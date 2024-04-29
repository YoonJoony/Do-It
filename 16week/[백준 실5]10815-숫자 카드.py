import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
targetArr = list(map(int, input().split()))


def binary_search(lst, target, start, end):
    global flag
    MID = (start + end) // 2
    if start > end:
        return

    if lst[MID] == target:
        flag = 1
        return
    elif lst[MID] < target:
        binary_search(lst, target, MID + 1, end)
    else:
        binary_search(lst, target, start, MID - 1)


for i, val in enumerate(targetArr):
    flag = 0
    binary_search(arr, val, 0, N)
    print(flag, end=" ")
