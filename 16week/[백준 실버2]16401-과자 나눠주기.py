# 입력 받기
M, N = map(int, input().split())  # M: 조카의 수, N: 과자의 수
snacks = list(map(int, input().split()))  # 각 과자의 길이

# 이진 탐색을 위한 시작점과 끝점 설정
start, end = 1, max(snacks)

# 이진 탐색 시작
result = 0
while start <= end:
    mid = (start + end) // 2  # 중간점 계산

    # mid 길이로 과자를 잘랐을 때, 몇 명에게 줄 수 있는지 계산
    count = sum(snack // mid for snack in snacks)

    if count >= M:  # 모든 조카에게 과자를 줄 수 있다면,
        result = mid  # 결과 업데이트
        start = mid + 1  # 더 긴 과자를 찾기 위해 시작점 조정
    else:  # 모든 조카에게 과자를 줄 수 없다면,
        end = mid - 1  # 더 짧은 과자를 찾기 위해 끝점 조정

# 결과 출력
print(result)
