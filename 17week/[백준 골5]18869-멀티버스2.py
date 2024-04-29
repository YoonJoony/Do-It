M, N = map(int, input().split())  # M: 우주의 수, N: 각 우주의 행성 수
patterns = []

for _ in range(M):
    universe = list(map(int, input().split()))
    # 각 우주에서 행성의 질량을 기준으로 정렬된 순서를 생성
    sorted_universe = sorted(set(universe))
    # 행성 질량을 그 질량의 정렬된 순서로 매핑 (동일 질량 처리)
    rank_map = {mass: rank for rank, mass in enumerate(sorted_universe)}
    # 각 행성의 순위로 구성된 패턴 생성
    pattern = tuple(rank_map[mass] for mass in universe)
    patterns.append(pattern)

# 같은 패턴을 가진 우주 쌍의 수 계산
pattern_count = 0
for i in range(M):
    for j in range(i + 1, M):
        if patterns[i] == patterns[j]:
            pattern_count += 1

print(pattern_count)
