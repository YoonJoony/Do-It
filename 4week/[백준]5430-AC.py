import sys
import re
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip('\n')
    st = []
    delete_count = 1
    n = int(input())
    num = re.findall(r'\d+', input().rstrip('\n'))

    for val in p:
        if val == "R":
            delete_count = 1
            if st and st[-1] == "R":
                st.pop()
            else:
                st.append(val)
        elif val == "D":
            if st and isinstance(st[-1], (int, float)):
                st.pop()
                delete_count += 1
                st.append(delete_count)
            else:
                st.append(delete_count)

    for val in st:
        if val == "R":
            num.reverse()
        else:
            if val > len(num):
                num = "error"
                break
            else:
                del num[0:val]

    if num != "error":
        print("[", end="")
        print(",".join(num), end="")
        print("]")
    else:
        print(num)