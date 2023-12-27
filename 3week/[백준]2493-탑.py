import sys
input = sys.stdin.readline

n = int(input())  # 탑의 개수
towers = list(map(int, input().split()))  # 각 탑의 높이
stack = []
result = [0] * n  # 수신 탑의 위치를 저장할 리스트

for i in range(n):
    # 스택이 비어있지 않고 현재 탑이 스택의 top에 있는 탑보다 높을 때까지
    while stack and towers[i] > towers[stack[-1]]:
        stack.pop()
    # 스택이 비어있지 않다면 현재 탑의 신호를 수신할 탑의 인덱스를 결과에 저장
    if stack:
        result[i] = stack[-1] + 1  # 인덱스는 0부터 시작하므로 +1
    # 현재 탑을 스택에 추가
    stack.append(i)

# 결과 출력
print(' '.join(map(str, result)))

