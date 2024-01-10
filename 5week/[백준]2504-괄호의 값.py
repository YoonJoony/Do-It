import sys

input = sys.stdin.readline

brackets = input().strip()
stack = []
result = 0
temp = 1

for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
        temp *= 2
    elif brackets[i] == '[':
        stack.append(brackets[i])
        temp *= 3
    elif brackets[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if brackets[i-1] == '(':
            result += temp
        stack.pop()
        temp //= 2
    elif brackets[i] == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if brackets[i-1] == '[':
            result += temp
        stack.pop()
        temp //= 3

if stack:
    result = 0

print(result)
