import sys

input = sys.stdin.readline

line = input().strip()
stack = []
answer = 0

for i in range(len(line)):
    if line[i] == '(':
        stack.append('(')
    else:  # ')' 일 때
        if line[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
