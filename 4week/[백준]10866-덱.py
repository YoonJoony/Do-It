import sys
from collections import deque
input = sys.stdin.readline

st = deque()

for _ in range(int(input())):
    command = list(input().split())

    if command[0] == "push_front":
        st.appendleft(command[1])
    elif command[0] == "push_back":
        st.append(command[1])
    elif command[0] == "pop_front":
        if st:
            print(st.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if st:
            print(st.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(st))
    elif command[0] == "empty":
        if st:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if st:
            print(st[0])
        else:
            print(-1)
    elif command[0] == "back":
        if st:
            print(st[len(st)-1])
        else:
            print(-1)

