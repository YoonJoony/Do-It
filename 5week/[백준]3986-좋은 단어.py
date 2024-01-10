import sys
input = sys.stdin.readline

count = 0
for _ in range(int(input())):
    line = list(input().strip())
    st = []
    i = 0
    while True:
        if len(line) < 2 or i == len(line)-1:
            break

        if i < len(line) -1 and line[i] == line[i+1]:
            del line[i]
            del line[i]
            i = 0
        else:
            i += 1

    if not line:
        count += 1

print(count)


