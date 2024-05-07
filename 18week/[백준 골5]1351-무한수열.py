N, P, Q = map(int, input().split())
dp = {0: 1}

def find(n):
    if n in dp:
        return dp[n]
    dp[n] = find(n // P) + find(n // Q)
    return dp[n]

print(find(N))
