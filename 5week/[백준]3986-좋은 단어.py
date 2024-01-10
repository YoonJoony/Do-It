import sys
input = sys.stdin.readline

count = 0
for _ in range(int(input())):
    line = input().strip()
    st = []
    for char in line:
        if st and st[-1] == char:
            st.pop()
        else:
            st.append(char)

    if not st:
        count += 1

print(count)
