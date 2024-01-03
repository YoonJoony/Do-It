import sys

input = sys.stdin.readline

while True:
    # strip은 띄어쓰기까지 제거되니 rstrip 엔터 키만 제거를 지정
    input_string = input().rstrip('\n')
    # 온전(".") 하나만 들어올 경우 종료
    if len(input_string) == 1 and input_string[0] == '.':
        break
    # 소괄호 대괄호만 골라내 자료형 변수에 저장
    output_string = ''.join(c for c in input_string if c in '()[]')
    # 소괄호 스택
    small = 0
    # 대괄호 스택
    big = 0
    # 밑에 for문으로 순서대로 괄호를 val에 입력하여 비교해준다.  스택
    # back_val은 전 순서에 저장된 괄호.
    back_val = ''

    for val in output_string:
        # small과 big이 0으로 떨어지지 않으면 균형잡힌 문자열이 아니다.
        if small == -1 or big == -1:
            break
        if val == '(':
            small += 1
        # ")" 소괄호가 닫이기 전 괄호는 열린 대괄호 "["가 될 수 없다.
        elif back_val != '[' and val == ')':
            small -= 1
        elif val == '[':
            big += 1
        # 대괄호 "]"가 닫기 전 괄호는 열린 소괄호 "("가 될 수 없다.
        elif back_val != '(' and val == ']':
            big -= 1
        else:
            small += 100
        back_val = val

    if small != 0 or big != 0:
        print("no")
    else:
        print("yes")

