# 입력 받기
N = int(input())  # 사람의 수
times = list(map(int, input().split()))  # 각 사람이 돈을 인출하는 데 필요한 시간

# 시간이 짧은 순서대로 정렬
times.sort()

# 필요한 총 시간 계산
total_time = 0
for i in range(N):
    total_time += times[i] * (N - i)

print(total_time)
