import heapq
N = int(input())

heap = []
for i in range(N):
    lst = list(map(int, input().split()))
    for val in lst:
        if i == 0:
            heapq.heappush(heap, val)
        else:
            if val > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, val)

print(heap[0])