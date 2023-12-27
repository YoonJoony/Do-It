import sys
input = sys.stdin.readline


st = []
for _ in range(int(input())):
    command = int(input())
    if command != 0:
        st.append(command)
    elif command == 0:
        if st:
            st.pop()

print(sum(st))