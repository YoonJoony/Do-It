import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr1 = deque()
arr2 = []
count = 1

for i in range(1, N+1):
    arr1.append(i)

while len(arr1) > 0:
    pop = arr1.popleft()
    if count == K:
        arr2.append(pop)
        count = 1
    else:
        arr1.append(pop)
        count += 1

print("<" + ", ".join(map(str, arr2))+ ">") # join 안에는 문자열만 들어감

# 1   1 2 3 4 5 6 7
# 2   2 3 4 5 6 7 1
# 3   3 4 5 6 7 1 2
#
# 1   4 5 6 7 1 2     3
# 2   5 6 7 1 2 4
# 3   6 7 1 2 4 5
#
# 1   7 1 2 4 5       6
# 2   1 2 4 5 7
# 3   2 4 5 7 1
#
# 1   4 5 7 1        2
# 2
# 3