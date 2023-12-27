import sys
input = sys.stdin.readline

st = []
for _ in range(int(input())):
    command = list(input().split())

    if command[0] == 'top':
        if st:
            pop = st.pop()
            print(pop)
            st.append(pop)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(st))
    elif command[0] == 'empty':
        if st:
            print(0)
        else:
            print(1)
    elif command[0] == 'pop':
        if st:
            print(st.pop())
        else:
            print(-1)
    else:
        st.append(command[1])