# 삼각형의 크기 입력 받기
n = int(input())
# 삼각형 데이터 입력 받기
triangle = [list(map(int, input().split())) for _ in range(n)]

# DP를 위한 초기화
# 첫 번째 줄은 입력 데이터 그대로 시작
for i in range(1, n):
    for j in range(len(triangle[i])):
        # 왼쪽 끝인 경우, 바로 위의 값만 더함
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        # 오른쪽 끝인 경우, 바로 위의 왼쪽 값만 더함
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i-1][j-1]
        # 그 외 중간에 위치한 경우, 위의 두 값 중 큰 값을 선택하여 더함
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

# 마지막 줄에서 최대값 찾기
print(max(triangle[n-1]))
