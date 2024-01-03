import sys
from collections import deque
input = sys.stdin.readline
st = deque()

for _ in range(int(input())):
    command = list(input().split())

    if command[0] == 'pop':
        if st:
            print(st.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(st))
    elif command[0] == 'empty':
        if st:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if st:
            print(st[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if st:
            st_pop = st.pop()
            print(st_pop)
            st.append(st_pop)
        else:
            print(-1)
    else:
        st.append(command[1])
