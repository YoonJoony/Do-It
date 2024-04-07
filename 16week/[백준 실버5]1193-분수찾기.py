#  1. 왼쪽이 1이 될 경우 오른쪽 1 증가
#  2. 오른쪽만 증가 하면 왼쪽 1증가 / 오른쪽 1 감소
#  3. 2번 과정으로 오른쪽이 1이 될 경우 왼쪽만 1 증가
#  4. 왼쪽만 증가하면 왼쪽 1 감소 오른쪽 1 증가
#  5. 4번 과정으로 왼쪽이 1이 될 경우 오른쪽 1 증가.
#  1번에서 X분수까지 다시 반복

X = int(input())

left, right = 1, 1
flag = 1 #  1일 경우 오른쪽만 증가 시킨 것, -1일 경우 왼쪽만 증가 시킨 것
cnt = 1
while cnt < X:
    if flag == 1:
        flag *= -1
        right += 1
        cnt += 1
        while right > 1 and cnt < X:
            left += 1
            right -= 1
            cnt += 1
    elif flag == -1:
        flag *= -1
        left += 1
        cnt += 1
        while left > 1 and cnt < X:
            left -= 1
            right += 1
            cnt += 1


print(f"{left}/{right}")
