# 규칙
# 최소 한개의 자음
# 최소 두개의 모음
# 암호는 사전순

# 모음은 1 ~ (l - 2) 개 까지만 존재 가능
# 자음은 2 ~ (l -1)개 까지만 존재 가능
import sys
input = sys.stdin.readline


def dfs(n, start):
    global cnt, result
    if n == L:
        for val in vowel:  # 모음이 1개 이상 혹은 L-2 만큼만 들어가도 됨
            if result.count(val):
                cnt += 1

        if 0 < cnt <= (L - 2):
            print(''.join(result))
        cnt = 0
        return

    for i in range(start, len(st)):
        result.append(st[i])
        dfs(n + 1, i + 1)
        result.pop()


L, C = map(int, input().split())
st = sorted(list(map(str, input().split())))
vowel = ['a', 'e', 'i', 'o', 'u']
result = []
cnt = 0
dfs(0, 0)
