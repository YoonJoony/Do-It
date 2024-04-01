import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())


def facto(n):
    if n <= 1:
        return n
    return n * facto(n-1)


arr = str(facto(N))
cnt = 0

# 왠지 모르겠지만 N이 0이면 답은 1이 아닌 0이다.
for i in range(len(arr)-1, -1, -1):
    if i != 0 and arr[i] == '0':
        cnt += 1
    else:
        break

print(cnt)