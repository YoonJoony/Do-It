from collections import deque
lst = deque([])

for _ in range(int(input())):
    word = input()
    if word not in lst:
        lst.append(word)

lst = sorted(lst, key=lambda x:(len(x), x))
print('\n'.join(lst))