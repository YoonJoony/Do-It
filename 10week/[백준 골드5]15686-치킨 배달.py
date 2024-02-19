from itertools import combinations


def get_chicken_distance(house, chicken_stores):
    return min(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]) for chicken in chicken_stores)


def solution(n, m, city_map):
    # flag = 0
    houses = [(i, j) for i in range(n) for j in range(n) if city_map[i][j] == 1]
    chickens = [(i, j) for i in range(n) for j in range(n) if city_map[i][j] == 2]

    # 모든 치킨집의 조합을 구한다.
    chicken_combinations = list(combinations(chickens, m))

    # if flag == 0:
    #     print(chicken_combinations)
    #     flag = 1

    # 각 조합에 대해 도시의 치킨 거리를 계산한다.

    # (2,2) 집에서 (1,2) 치킨집까지의 거리: |2-1| + |2-2| = 1
    # (2,2) 집에서 (2,1) 치킨집까지의 거리: |2-2| + |2-1| = 1
    # (2,2) 집에서 (4,4) 치킨집까지의 거리: |2-4| + |2-4| = 4
    # 가장 가까운 거리는 1이므로 집의 치킨 거리는 1.
    # 이렇게 집 들마다 치킨 집 조합의 각각 치킨 집마다 최소 치킨 거리를 구한다.
    min_distance = float('inf') # float('inf') : 무한대를 나타냄.
    for comb in chicken_combinations:
        min_distance = min(min_distance, sum(get_chicken_distance(house, comb) for house in houses))

    return min_distance


# 입력
n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]

# 솔루션 함수 호출 및 출력
print(solution(n, m, city_map))
