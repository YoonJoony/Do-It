import sys
input = sys.stdin.readline

N = int(input())
minus_arr = []
plus_arr = []
result = 0

arr = sorted([int(input().strip('\n')) for _ in range(N)], reverse=True)
arr = [plus_arr.append(item) if item*-1 < 0 else minus_arr.append(item) for item in arr]

# 양수인 경우 2개씩 묶기
for i in range(0, len(plus_arr), 2):
    if i < len(plus_arr) - 1:
        if 1 not in (plus_arr[i], plus_arr[i+1]):
            result += plus_arr[i] * plus_arr[i+1]
        else:
            result += plus_arr[i] + plus_arr[i+1]
    else:
        result+=plus_arr[i]

# 음수인 경우 2개씩 묶기
for i in range(len(minus_arr)-1, -1, -2):
    if i > 0:
        result += minus_arr[i] * minus_arr[i-1]
    else:
        result += minus_arr[i]

print(result)