import sys
input = sys.stdin.readline

while True:
    st = []
    query = input().rstrip('\n')
    if len(query) == 1 and query[0] == '.':
        break
    list = "".join(c for c in query if c in "()[]")
    for val in list:
        if st and val == ")" and st[-1] != "[":
            if st[-1] == "(":
                st.pop()
        elif st and val == "]" and st[-1] != "(":
            if st[-1] == "[":
                st.pop()
        else:
            st.append(val)

    if st:
        print("no")
    else:
        print("yes")
