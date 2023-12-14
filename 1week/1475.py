#백준 방 번호

N = str(input())

numbers =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 1

for i in range(len(N)):
    if i < len(N) - 1 and N[i] == N[i+1]:
        count += 1

    if N[i] == 9:


print(count)
# 1 : 1, 2 : 1, 3 : 2: ,4 : 2, 5: 3, 6 : 3