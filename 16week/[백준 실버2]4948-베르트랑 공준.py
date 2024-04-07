import sys
from collections import deque

input = sys.stdin.readline

num = 123456
max_root = 1
i = 2

while i * i <= 2 * num:
    max_root += 1
    i += 1

arr = [_ for _ in range(2, (2 * num) + 1)]

MIN = 1
while MIN <= max_root:
    MIN += 1
    arr = list(filter(lambda x: x % MIN != 0 or x == MIN, arr))

while True:
    X = int(input())

    if X == 0:
        break

    i = 0
    cnt = 0
    while i < len(arr) and arr[i] <= 2*X:
        if arr[i] > X:
            cnt += 1
        i += 1

    print(cnt)