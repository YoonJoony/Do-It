import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

meeting = sorted(meeting, key=lambda x:(x[1], x[0]))

end_time = meeting[0][1]
cnt = 1
for i in range(1, N):
    if end_time <= meeting[i][0]:
        end_time = meeting[i][1]
        cnt += 1

print(cnt)