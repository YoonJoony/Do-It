# 삼각형의 크기 입력 받기
n = int(input())
# 삼각형 데이터 입력 받기
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if (j-1) < 0:
            triangle[i][j] += triangle[i-1][j]
        elif (j-1) >= 0 and (j+1) < i+1:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        else:
            triangle[i][j] += triangle[i-1][j-1]

print(max(triangle[n-1]))