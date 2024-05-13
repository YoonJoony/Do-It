import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())  # 보석의 수 N, 가방의 수 K
jewels = [list(map(int, input().split())) for _ in range(N)]  # (무게, 가치)
bags = [int(input()) for _ in range(K)]  # 가방의 최대 무게

# 무게를 기준으로 보석 정렬
jewels.sort()

# 가방도 무게 제한에 따라 정렬
bags.sort()

total_value = 0  # 총 가치
temp_jewels = []  # 현재 가방에 넣을 수 있는 보석들

j = 0  # 보석 인덱스
for bag in bags:
    # 현재 가방에 넣을 수 있는 모든 보석을 temp_jewels에 추가
    while j < N and jewels[j][0] <= bag:
        # 보석의 가치를 최대 힙에 넣음 (가치, 무게)
        heapq.heappush(temp_jewels, -jewels[j][1])
        j += 1

    # temp_jewels 중에서 가장 가치가 높은 보석을 꺼내서 total_value에 추가
    if temp_jewels:
        total_value -= heapq.heappop(temp_jewels)

print(total_value)
