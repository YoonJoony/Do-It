import sys
from collections import deque
input = sys.stdin.readline

st = deque()

N, M = map(int, input().split())
# 주어진 원소
select_num = list(map(int, input().split()))
# 연산의 최솟값
count = 0
for i in range(1, N+1):
    st.append(i)

# 큐 길이가 홀수 및 짝수 구분 변수
x = 0

while len(select_num) > 0:
    # 큐가 짝수일 경우 아닐경우 조건
    if len(st) % 2 == 0:
        x = 0
    else:
        x = 1

    # 첫번째 큐 원소랑 뽑고자 하는 첫 원소랑 같을 경우
    if select_num[0] == st[0]:
        select_num.remove(st[0]) # 뽑았으니 뽑은 원소는 지워준다.
        st.popleft() # 큐도.
    else: # 2번 3번을 통합한다. 단 뽑고자 하는 원소의 위치 조건을 주어 효율적으로 탐색한다.
        select_num_index = st.index(select_num[0])+1
        if select_num_index <= len(st) // 2 + x:
            st_popleft = st.popleft()
            st.append(st_popleft)
            count += 1
        else:
            st_pop = st.pop()
            st.appendleft(st_pop)
            count += 1
print(count)