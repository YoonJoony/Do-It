# 백준 방 번호

N = str(input())

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 1
flag = 0

for i in range(len(N)):
    if i < len(N) - 1 and N[i] == N[i + 1] and flag == 0:
        count += 1

    if int(N[i]) == 9:
        flag == 1

print(count)
