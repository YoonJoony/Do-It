# 계단의 개수 입력 받기
n = int(input())
# 각 계단의 점수 저장
stairs = [0] * 300
for i in range(n):
    stairs[i] = int(input())

# dp 테이블 초기화
dp = [0] * 300

# 초기값 설정, 계단 인덱스마다 밟았을 때의 최대값을 넣어줘야됨.
dp[0] = stairs[0] # 첫번째 계단은 그대로
dp[1] = stairs[0] + stairs[1] # 두번째 계단은 당연히 첫번째, 두번째 밟은게 최대값
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
# 세번째는 연속으로 못밟으니 첫번째 + 세번째 or 두번째 + 세번째 최대값

# DP로 결과 찾기
# dp 배열 4번째부터 계단을 밟았을 경우 중 최대값을 넣어준다.
# 4번째부터 계단을 밟을 경우는 두 가지가 있음. 연속 세번을 못밟으니
# 1. 현재 계단 -2번째에서 한 계단 건너 뛰어야 함.
# 2. 현재 계단 -3번째에서 현재 계단 -1 계단까지 건너 뛰어야 함
for i in range(3, n):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

# 결과 출력
print(dp)
