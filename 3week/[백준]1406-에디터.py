import sys
input = sys.stdin.readline

st1 = list(input().rstrip()) # 끝 개행문자 제거하여 리스트에 문자열 개별로 추가
st2 = [] # 커서 이동 시 이동할 때 거친 문자를 담을 스택을 저장. => 나중에 reversed()로 st1과 합친다.

for _ in range(int(input())):
    command = list(input().split()) # 문자열 입력 받음
    if command[0] == 'L': # 'L'일 경우 st1 끝 문자 pop 한걸 st2에 추가.
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D': # 'R'일 경우 st2 끝 문자 pop 한걸 st2에 추가.
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B': # 왼쪽 문자 삭제 st1 pop
        if st1:
            st1.pop()

    else:
        st1.append(command[1]) # P $ 일 경우 $ 문자를 st1 끝에 추가함.

st1.extend(reversed(st2)) # 스택 두개를 합친다.
print(''.join(st1))