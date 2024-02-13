def power_mod(a, b, c):
    if b == 0:
        return 1
    half = power_mod(a, b // 2, c)
    half_squared = (half * half) % c

    if b % 2:
        return (half_squared * a) % c
    else:
        return half_squared


# 입력 받기
A, B, C = map(int, input().split())

# 결과 출력
print(power_mod(A, B, C))
