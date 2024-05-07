import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    min_heap, max_heap = [], []
    lazy_deleted = {}  # 지연 삭제를 위한 딕셔너리
    for _ in range(int(input())):
        transaction, n = input().split()
        n = int(n)

        if transaction == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            if n not in lazy_deleted:
                lazy_deleted[n] = 0
            lazy_deleted[n] += 1
        else:
            heap = max_heap if n == 1 else min_heap
            while heap and lazy_deleted[-heap[0] if n == 1 else heap[0]] == 0:
                heapq.heappop(heap)
            if heap:
                lazy_deleted[-heap[0] if n == 1 else heap[0]] -= 1

    # 최종적으로 유효한 최소값과 최대값 찾기
    while min_heap and lazy_deleted[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and lazy_deleted[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
