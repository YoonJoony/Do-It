# 이진/이분 탐색
def binary_search(array, target):
    # 시작, 끝
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2  # 중간
        if array[mid] < target:  # 타겟이 중간보다 같거나 클 경우
            start = mid + 1  # 시작을 중간에서 + 1로 함.
        else:  # 아닐경우 끝을 중간 -1로 함.
            end = mid - 1
    return start


def solve(A, B):
    B.sort()
    answer = 0
    for a in A:
        answer += binary_search(B, a)
    return answer


T = int(input())  # 테스트 케이스의 수
for _ in range(T):
    _, _ = map(int, input().split())  # A와 B의 크기(사용하지 않음)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve(A, B))
