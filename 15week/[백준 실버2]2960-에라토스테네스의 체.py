N, K = map(int, input().split())
arr = [_ for _ in range(2, N+1)]
result = []

while True:
    P = min(arr)
    # P의 배수를 전부 result에 추가
    result += (list(filter(lambda x:x % P == 0, arr)))
    # arr 배열에서 result에 들어간 값을 빼고 초기화
    arr = [item for item in arr if item not in result]
    # K번째 지워진 수가 result 크기와 같거나 작다면 종료
    if K <= len(result):
        break

print(result[K-1])