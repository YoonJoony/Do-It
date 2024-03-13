import copy

# 4개의 톱니바퀴 상태를 입력 받음
gear = [list(input().strip('\n')) for _ in range(4)]
# 톱니바퀴의 복사본을 생성하여 회전 시 원본 데이터 손상 방지
g = copy.deepcopy(gear)

# 최종 점수를 저장할 변수
result = 0


def start():
    global rotation, g, gear
    # 선택된 톱니바퀴를 회전시킴
    g = gear_rotation(g, rotation, gearName)
    # 왼쪽, 오른쪽 톱니바퀴의 회전 가능성 판단 플래그
    l_flag = 1
    r_flag = 1
    for i in range(1, 5):
        # 회전 방향 전환
        rotation *= -1
        # 왼쪽 톱니바퀴 회전 가능성 판단 및 회전 실행
        if l_flag == 1 and gearName - i >= 0 and gear[gearName - (i - 1)][6] != gear[gearName - i][2]:
            g = gear_rotation(g, rotation, gearName - i)
        else:
            l_flag = 0
        # 오른쪽 톱니바퀴 회전 가능성 판단 및 회전 실행
        if r_flag == 1 and gearName + i < 4 and gear[gearName + (i - 1)][2] != gear[gearName + i][6]:
            g = gear_rotation(g, rotation, gearName + i)
        else:
            r_flag = 0


# 톱니바퀴 회전 함수
def gear_rotation(g, r, gear_num):
    # 시계 방향 회전
    if r == 1:
        gear_index = g[gear_num][7]
        for i in range(7, 0, -1):
            g[gear_num][i] = g[gear_num][i - 1]
        g[gear_num][0] = gear_index
    # 반시계 방향 회전
    else:
        gear_index = g[gear_num][0]
        for i in range(1, 8, 1):
            g[gear_num][i - 1] = g[gear_num][i]
        g[gear_num][7] = gear_index

    return g

# 회전 명령 입력 받음
for _ in range(int(input())):
    gearName, rotation = map(int, input().split())
    # 톱니바퀴 번호 조정 (0부터 시작)
    gearName -= 1

    # 회전 시작
    start()
    # 바뀐 톱니바퀴를 원본 톱니바퀴에 상태 갱신
    gear = copy.deepcopy(g)

# 최종 점수 계산
score = [1, 2, 4, 8]
for i in range(4):
    if g[i][0] == '1':
        result += score[i]
# 결과 출력
print(result)
