N, C = map(int, input().split())

lst = list(map(int, input().split()))
lst2 = []
tp = []
for val in lst:
    if val not in lst2:
        lst2.append(val)


for i in range(len(lst2)):
    tp.append((lst2[i], lst.count(lst2[i])))

tp = sorted(tp, key=lambda x:x[1], reverse=True)

for i in range(len(tp)):
    print(''.join((str(tp[i][0]) + ' ') * tp[i][1]), end='')