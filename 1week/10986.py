# 백준 나머지 합

N, M = map(int, input().split())


array = list(map(int, input().split()))
array2 = []
count = 0

array_sum = 0

for i in range(N):
    array2.append(sum(array))


for i in range(N):
    for j in range(i, N):
        array_sum += array[j]
        if array_sum % M == 0:
            print(array_sum)
            count += 1
    array_sum = 0

print(count)