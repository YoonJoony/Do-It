N, M = map(int, input().split())

sequence = []


def backtrack(depth):
    if depth == M:  # M개를 모두 선택했다면 출력
        print(' '.join(map(str, sequence)))
        return

    for i in range(1, N + 1):  # 1부터 N까지의 숫자 중에서 선택
        sequence.append(i)  # 현재 숫자를 수열에 추가
        backtrack(depth + 1)  # 다음 숫자를 선택하기 위해 재귀 호출
        sequence.pop()  # 백트래킹, 마지막에 추가한 숫자를 제거하고 이전 단계로 돌아감


backtrack(0)  # 백트래킹 시작
