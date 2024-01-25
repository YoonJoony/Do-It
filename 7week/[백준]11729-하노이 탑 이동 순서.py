def hanoi(n, start, target, aux):
    if n == 1:
        print(start, target)  # 가장 작은 원반을 목표 기둥으로 이동
        return

    # Step 1: n-1개의 원반을 aux 기둥으로 이동
    hanoi(n - 1, start, aux, target)

    # Step 2: 가장 큰 원반을 target 기둥으로 이동
    print(start, target)

    # Step 3: aux 기둥에 있는 n-1개의 원반을 target 기둥으로 이동
    hanoi(n - 1, aux, target, start)


n = int(input())  # 사용자로부터 원반의 수를 입력받음
print(2 ** n - 1)  # 총 이동해야 하는 횟수를 계산하여 출력

# 재귀 함수 호출 (1번 기둥에서 3번 기둥으로 n개의 원반을 이동)
hanoi(n, 1, 3, 2)
