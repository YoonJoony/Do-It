import copy

gear = [list(input().strip('\n')) for _ in range(4)]
g = copy.deepcopy(gear)
ans = 0


def start():
    global rotation, g, gear
    g = gear_rotation(g, rotation, gearName)
    l_flag = 1
    r_flag = 1
    for i in range(1, 5):
        rotation *= -1
        if l_flag == 1 and gearName - i >= 0 and gear[gearName - (i - 1)][6] != gear[gearName - i][2]:
            g = gear_rotation(g, rotation, gearName - i)
            l_flag = 1
        else:
            l_flag = 0
        if r_flag == 1 and gearName + i < 4 and gear[gearName + (i - 1)][2] != gear[gearName + i][6]:
            g = gear_rotation(g, rotation, gearName + i)
            r_flag = 1
        else:
            r_flag = 0


def gear_rotation(g, r, gear_num):
    if r == 1:
        gear_index = g[gear_num][7]
        for i in range(7, 0, -1):
            g[gear_num][i] = g[gear_num][i - 1]
        g[gear_num][0] = gear_index
    else:
        gear_index = g[gear_num][0]
        for i in range(1, 8, 1):
            g[gear_num][i - 1] = g[gear_num][i]
        g[gear_num][7] = gear_index

    return g


for _ in range(int(input())):
    gearName, rotation = map(int, input().split())
    gearName -= 1

    start()
    gear = copy.deepcopy(g)


result = 0
score = [1, 2, 4, 8]
for i in range(4):
    if g[i][0] == '1':
        result += score[i]
print(result)
