A, B = map(int, input().split())
A_arr = sorted(list(map(int, input().split())))
B_arr = sorted(list(map(int, input().split())))


def binary_search(lst, target, start, end):
    MID = (start + end) // 2

    if start > end:
        return True

    if lst[MID] == target:
        return False
    elif lst[MID] < target:
        return binary_search(lst, target, MID + 1, end)
    else:
        return binary_search(lst, target, start, MID - 1)


result = []
for val in A_arr:
    if binary_search(B_arr, val, 0, B-1):
        result.append(val)

if result:
    print(len(result))
    print(*result)
else:
    print(0)
