from itertools import combinations


def get_chicken_distance(house, chicken_stores):
    return min(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]) for chicken in chicken_stores)


def solution(n, m, city_map):
    houses = [(i, j) for i in range(n) for j in range(n) if city_map[i][j] == 1]
    chickens = [(i, j) for i in range(n) for j in range(n) if city_map[i][j] == 2]

    # 모든 치킨집의 조합을 구한다.
    chicken_combinations = list(combinations(chickens, m))

    # 각 조합에 대해 도시의 치킨 거리를 계산한다.
    min_distance = float('inf')
    for comb in chicken_combinations:
        min_distance = min(min_distance, sum(get_chicken_distance(house, comb) for house in houses))

    return min_distance


# 입력
n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]

# 솔루션 함수 호출 및 출력
print(solution(n, m, city_map))
