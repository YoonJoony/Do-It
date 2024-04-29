n = int(input())  # 용액의 개수
solutions = list(map(int, input().split()))  # 용액들
solutions.sort()  # 용액 정렬

left, right = 0, n - 1  # 투 포인터 초기화
answer = [left, right]  # 정답을 저장할 변수 (인덱스 형태로 저장)
min_diff = float('inf')  # 가능한 최대 차이값으로 초기화

while left < right:
    current_sum = solutions[left] + solutions[right]  # 현재 두 용액의 합

    # 현재 합의 절대값이 이전 최소값보다 작으면 갱신
    if abs(current_sum) < min_diff:
        min_diff = abs(current_sum)
        answer = [left, right]

    # 합이 0보다 크면 right를 줄여 합을 감소시킴
    if current_sum > 0:
        right -= 1
    # 합이 0보다 작으면 left를 늘려 합을 증가시킴
    elif current_sum < 0:
        left += 1
    # 합이 0이면 가장 가까운 값이므로 바로 종료
    else:
        break

# 정답 출력 (용액의 실제 값)
print(solutions[answer[0]], solutions[answer[1]])