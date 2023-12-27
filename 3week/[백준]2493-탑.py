import sys
input = sys.stdin.readline

top = list(map(int, input().split()))
arr = []
arr.extend(reversed(top))
st = []
count = 1

for i in range(len(arr)):
    if i < len(arr)-1 and arr[i] <= arr[i+1]:
        for j in range(count):
            st.append(top.index(arr[i+1]) + 1)
            count = 1
    else:
        count += 1

for i in range(len(arr)-len(st)):
    st.append(0)

print(" ".join(map(str, st)))
