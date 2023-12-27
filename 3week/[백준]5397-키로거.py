import sys

input = sys.stdin.readline

for _ in range(int(input())):
    command = list(input().rstrip())
    st1 = []
    st2 = []

    for i in range(len(command)):
        if command[i] == '<':
            if st1:
                st2.append(st1.pop())
        elif command[i] == '>':
            if st2:
                st1.append(st2.pop())
        elif command[i] == '-':
            if st1:
                st1.pop()
        else:
            st1.append(command[i])
    st1.extend(reversed(st2))
    print("".join(st1))
