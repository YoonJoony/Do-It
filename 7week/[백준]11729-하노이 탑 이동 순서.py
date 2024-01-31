def hanoi(n, start, mid, to):
    # 이동할 원판의 수가 1개 일때 (탈출 조건)
    if n == 1:
        print(start, to)
        return

    # 1 -> 2로 n-1 개를 옮김.
    # 위 1번 과정
    hanoi(n - 1, start, to, mid)

    # 가장 큰 원판을 목적 지점으로 옮김
    # 위 2번 과정
    print(start, to)

    # 2 -> 3으로 n-1 개를 옮김
    # 위 번 과정
    hanoi(n - 1, mid, start, to)


n = int(input())  # 사용자로부터 원반의 수를 입력받음
print(2 ** n - 1)  # 총 이동해야 하는 횟수를 계산하여 출력

# 재귀 함수 호출 (1번 기둥에서 3번 기둥으로 n개의 원반을 이동)
hanoi(n, 1, 2, 3)
