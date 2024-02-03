import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def star_ten(size):
    if size == 1:
        return ['*']

    Stars = star_ten(size // 3)
    L = []

    # 원본 배열 생성
    for S in Stars:
        L.append(S * 3)
    for S in Stars:
        L.append(S + " " * (size // 3) + S)
    for S in Stars:
        L.append(S * 3)
    return L # 원본 배열 리턴


n = int(input())
print('\n'.join(star_ten(n)))
