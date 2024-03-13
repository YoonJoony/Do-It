N, C = map(int, input().split())

lst = list(map(int, input().split()))
lst2 = []
tp = []

# 중복 제거한 값만 있는 배열
for val in lst:
    if val not in lst2:
        tp.append((val, lst.count(val)))

# 투플 생성 (x = 값, y = 빈도)
for i in range(len(lst2)):
    tp.append((lst2[i], lst.count(lst2[i])))

# 1. 빈도 순으로 정렬
tp = sorted(tp, key=lambda x:x[1], reverse=True)

for i in range(len(tp)):
    print(''.join((str(tp[i][0]) + ' ') * tp[i][1]), end='')