import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip('\n'))) for _ in range(N)]
print(graph)