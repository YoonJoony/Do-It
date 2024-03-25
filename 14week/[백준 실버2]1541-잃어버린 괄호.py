import sys
input = sys.stdin.readline

A = str(input().strip('\n'))
st = ''
result = []
answer = 0
for val in A:
    if st and st[0] == '0':
        continue
    elif val in '0123456789+':
        st += val
    elif val == '-':
        result.append(st)
        st = ''

result.append(st)

print(result)
for i in range(len(result)):
    result[i] = eval(result[i])

answer = result[0]

for i in range(1, len(result)):
    answer -= result[i]

print(answer)