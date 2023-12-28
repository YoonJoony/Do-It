N = int(input())
arr2 = []
arr = []
st = []
for i in range(N):
    arr2.append(int(input()))

arr.extend(reversed(arr2))

i = 1
st.append(1)
print("+")

while i <= N:
    if st and st[-1] == arr[-1]:
        arr.pop()
        st.pop()
        print("-")
    elif i < N:
        i += 1
        st.append(i)
        print("+")
