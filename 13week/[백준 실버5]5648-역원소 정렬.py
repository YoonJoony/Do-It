from collections import deque
lst = deque(list(map(int, input().split())))

N = lst.popleft()


def chainge(l):
    chainge_lst = deque([])
    while l:
        v = l.popleft()
        str_val = str(v)
        temp = ''
        for j in range(len(str_val)-1, -1, -1):
            if not temp and str_val[j] == '0':
                continue
            temp += str_val[j]
        chainge_lst.append(int(temp))
    return chainge_lst


while len(lst) < N:
    arr = list(map(int, input().split()))
    lst += arr

lst = sorted(chainge(lst))
for val in lst:
    print(val)
