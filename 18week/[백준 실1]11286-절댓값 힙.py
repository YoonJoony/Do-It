import sys
import heapq
input = sys.stdin.readline
N = int(int(input()))
heap = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
        # 첫 번째 요소를 기준으로 비교
        # 값이 같을 경우 두 번째 요소랑 비교
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
