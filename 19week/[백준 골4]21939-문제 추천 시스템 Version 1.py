from collections import defaultdict
import heapq
max_heap = []
min_heap = []
deleted = defaultdict(int)

for _ in range(int(input())):
    x, y = map(int, input().split())
    heapq.heappush(max_heap, (-y, -x))
    heapq.heappush(min_heap, (y, x))
    deleted[x] += 1

for _ in range(int(input())):
    lst = list((input().split()))
    if lst[0] == "add":
        x, y = int(lst[1]), int(lst[2])
        heapq.heappush(max_heap, (-y, -x))
        heapq.heappush(min_heap, (y, x))
        deleted[int(lst[1])] += 1
    elif lst[0] == "solved":
        deleted[int(lst[1])] -= 1
        while max_heap and deleted[-max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
        while min_heap and deleted[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
    else:
        heap = []
        if lst[1] == "1":
            heap = max_heap
            while heap and deleted[-heap[0][1]] == 0:
                heapq.heappop(heap)
            print(-heap[0][1])
        else:
            heap = min_heap
            while heap and deleted[heap[0][1]] == 0:
                heapq.heappop(heap)
            print(heap[0][1])
