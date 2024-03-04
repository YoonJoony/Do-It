import sys
input = sys.stdin.readline
# A의 가장 큰 수를 B와 비교
# B의 가장 작은 수를 다음 A의 가장 큰 수와 비교
# if 다음 A의 수가 B의 가장 작은 수보다 크다면 진행 else 노 진행

for _ in range(int(input())):
    N, M = map(int, input().split())
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))
    min_B = B_lst[0]
    sm = 0
    cnt = 0
    for i in range(len(A_lst)):
        n = 0
        if i != 0 and A_lst[i] < min_B:
            continue
        while n < len(B_lst):
            if min_B > B_lst[n]:
                min_B = B_lst[n]
            if A_lst[i] > B_lst[n]:
                cnt += 1
            n += 1

    print(cnt)