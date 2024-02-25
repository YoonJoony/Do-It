from collections import deque

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

flag = 0
result = 0
for i in range(N):
    lst2 = deque(lst[:])
    sm = 0
    q = [lst2[(N-1) - i]]
    lst2.remove(q[0])

    for j in range(N):
        if len(q) == N:
            for k in range(N):
                if k < N - 1:
                    sm += abs(q[k] - q[k+1])

            result = max(result, sm)
            continue

        if flag == 0:
            q.append(lst2.popleft())
            flag = 1

        else:
            q.append(lst2.pop())
            flag = 0

print(result)
