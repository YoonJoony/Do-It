import sys

input = sys.stdin.readline

# M = int(input())
sum = 0

def cal(N):
    global sum

    if N == 0:
        return sum

    for i in range(1, N + 1):
        if N % i == 0:
            sum += i

    N -= 1
    return cal(N)


if __name__ == '__main__':
    # for i in range(M):
    N = int(input())
    sum = 0
    print(cal(N))