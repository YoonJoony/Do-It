import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
cnt = 0

M = [[_ for _ in range(N ** 2)] for _ in range(N ** 2)]
for i in range(N ** 2):
    for j in range(N ** 2):
        M[i][j] = cnt
        cnt += 1


f_graph = []

#  배열 첫 번째 원소와 배열 크기만큼의 첫 번째 원소에 들어갈 크기 x=2^2, y=2^3//x = 2^4, y =  2^5 // y = 2^6, 2^7
# N = 2 => 2, 3 // N = 3 => 4, 5 // N = 4 => 6, 7 // N = 5 => 8, 9 // N = 6 => 10, 11
# N + (N - 2), N + (N-2) + 1
# 배열 개수 => K = 1 , 2*2개, K = 2 , 4*4개 K = 3 , 8*8개
def resource(graph, K):
    if K == N:
        return graph
    graph_area = 2**(K-1) # K = 2 => 2*2 K = 3 => 4*4 K = 4 => 8*8

    graph = [[_ for _ in range(graph_area)] for _ in range(graph_area)]

    for i in range(graph_area):
        for j in range(graph_area):


    return resource(graph, N + (N - 2))


result_graph = resource(f_graph, 2)
