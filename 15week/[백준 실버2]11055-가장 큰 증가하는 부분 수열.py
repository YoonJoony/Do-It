N = int(input())
arr = list(map(int, input().split()))
DP = arr[:]  # DP 배열을 arr의 복사본으로 초기화

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j] + arr[i])
print(max(DP))
