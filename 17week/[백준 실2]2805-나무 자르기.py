N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

start, end = 1, max(arr)
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = sum(item - mid for item in arr if item > mid)

    if cnt >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
