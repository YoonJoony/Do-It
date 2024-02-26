from collections import deque
n, w, L = map(int, input().split())
queue = deque(list(map(int, input().split())))
# lst : 다리에 진입한 트럭
lst = deque([0] * (w + 1)) # w + 1개인 이유 : 배열을 앞으로 밀 때마다 맨 앞 배열에 넣을 트럭이 없을 경우 0으로 설정하기 위해.
sm = deque([])
time_cnt = 0

# 트럭이 전부 지나간 경우 while 빠져나옴
while queue or sum(lst) != 0:
    i = 0 # i는 w를 카운트 하는 변수. (다음 차가 앞의 차 무게때문에 못들어올 경우 만들어줌)
          # 무게가 7인 트럭이 처음 들어오면 i = 1이 된다.
          # 20번째 조건문으로 다음 트럭은 못들어오므로 i가 w미만이 될 때까지 그대로 다시 i에 1을 더해줌.
    while i < w:

        # 시간이 지날때마다 다리에 있는 트럭을 앞으로 당긴다.
        # start : 끝에서부터, end : 0번째까지, 감소하면서
        for i in range(len(lst)-1, 0, -1):
            lst[i] = lst[i - 1]

        i += 1
        time_cnt += 1

        # '기존 다리에 진입한 트럭'과 '진입할 트럭(큐 가장 왼쪽)'의 합이 다리 무게보다 작을 경우
        if queue and sum(lst) + queue[0] <= L:
            if lst and queue and lst[0] != queue[0]:
                i = 0 # 새로운 트럭이 들어올 때마다 i의 값을 초기화.
            lst[1] = queue.popleft()  # 다리에 트럭 진입.

        if not queue:  # 큐가 다 빠졌을 경우
            break

print(time_cnt)