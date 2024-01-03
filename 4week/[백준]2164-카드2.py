import sys
from collections import deque
input = sys.stdin.readline
st = deque()
flag = 0

N = int(input())

for i in range(1, N+1):
    st.append(i)

while len(st) > 1:
    if flag == 0:
        st.popleft()
        flag = 1
    else:
        st_popLeft = st.popleft()
        st.append(st_popLeft)
        flag = 0

print(st.pop())