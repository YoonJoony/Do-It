import heapq
N = int(input())
heap = []
[heapq.heappush(heap, int(input())) for _ in range(N)]

result = 0
while heap and N > 1:
    sm = 0
    for i in range(2):
        if heap:
            sm += heapq.heappop(heap)
    result += sm
    if heap:
        heapq.heappush(heap, sm)

print(result)










