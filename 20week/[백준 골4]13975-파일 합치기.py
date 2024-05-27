import heapq

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    heap = []
    for i in range(N):
        heapq.heappush(heap, A[i])
    result = 0

    while True:
        combine = 0
        for _ in range(2):
            if heap:
                combine += heapq.heappop(heap)

        result += combine
        if not heap:
            break
        heapq.heappush(heap, combine)

    print(result)