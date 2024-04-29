# 백준 3151번 합이 0

n = int(input())  # 학생 수 입력
students = list(map(int, input().split()))  # 학생들의 키 입력
students.sort()  # 키 순서대로 정렬

count = 0  # 합이 0이 되는 조합의 수

# i는 첫 번째 학생을 가리키는 인덱스
for i in range(n-2):
    # 두 포인터 초기화
    left, right = i+1, n-1
    while left < right:  # 두 포인터가 만나지 않을 때까지 반복
        total = students[i] + students[left] + students[right]
        # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
        if total < 0:
            left += 1
        # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
        elif total > 0:
            right -= 1
        # 합이 0인 경우
        else:
            # 중복 요소 처리
            if students[left] == students[right]: # 만약 왼쪽 값과 오른쪽 값이 같다면, 그 사이의 모든 조합이 가능
                count += (right - left + 1) * (right - left) // 2 # 조합의 수를 계산
                break # 더 이상 탐색할 필요가 없으므로 반복문 탈출
            else:
                # 왼쪽 값과 오른쪽 값이 다른 경우, 중복되는 값의 개수를 세어야 함
                l, r = left, right
                # 왼쪽 값이 같은 동안 왼쪽 포인터 이동
                while students[l] == students[left] and l < right:
                    l += 1
                # 오른쪽 값이 같은 동안 오른쪽 포인터 이동
                while students[r] == students[right] and r > left:
                    r -= 1
                # 가능한 조합의 수를 계산하여 추가
                count += (l - left) * (right - r)
                # 포인터 업데이트
                left = l
                right = r

print(count)