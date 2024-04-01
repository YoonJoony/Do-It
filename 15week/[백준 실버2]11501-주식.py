import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    i = 0

    while arr and i < len(arr):
        max_index = arr.index(max(arr[i:]))
        if i < max_index:
            result += arr[max_index] * (max_index-i) - sum(arr[i:max_index])
            arr[0:max_index+1] = []
            i = 0
        else:
            i += 1

    print(result)