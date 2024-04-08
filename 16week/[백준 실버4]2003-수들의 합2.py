N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, pv = 0, 1

sm = arr[0]
cnt = 0
while pv < N+1:
    if sm == M:
        sm -= arr[start]
        cnt += 1
        start += 1
        pv += 1
        sm = sum(arr[start:pv])
    elif sm < M:
        pv += 1
        sm = sum(arr[start:pv])
    else:
        sm -= arr[start]
        start += 1

print(cnt)