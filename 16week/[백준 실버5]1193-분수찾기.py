#  1. 왼쪽이 1이 될 경우 오른쪽 1 증가
#  2. 오른쪽만 증가 하면 왼쪽 1증가 / 오른쪽 1 감소
#  3. 2번 과정으로 오른쪽이 1이 될 경우 왼쪽만 1 증가
#  4. 왼쪽만 증가하면 왼쪽 1 감소 오른쪽 1 증가
#  5. 4번 과정으로 왼쪽이 1이 될 경우 오른쪽 1 증가.
#  1번에서 X분수까지 다시 반복

X = int(input())

line = 0
max_num = 0
while X > max_num:
    line += 1
    max_num += line

gap = max_num - X
if line % 2 == 0:
    numerator = line - gap
    denominator = gap + 1
else:  # 대각선 총 개수와 X 차이가 0일때 홀수 대각선일 경우.
    # 홀수 대각선의 분자는 점점 감소함으로 차이가 0이 난다는 것은, 즉 분자는 1이다.
    # 홀수 대각선의 분모는 점점 늘어남으로 line(나올 수 있는 최대 수) - 차이 따라서,
    # 홀수일 경우는 [분자 -> 차이 + 1, 분모 -> line - 차이]
    # 짝수는 반대로 수행.
    numerator = gap + 1
    denominator = line - gap

print(f"{numerator}/{denominator}")
