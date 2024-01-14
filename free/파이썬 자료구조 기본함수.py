import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

st = "Hello World"

print(st[::-1])

l = ["hello", "world", "fuck"]
print(" ".join(l))

# join() 함수
l = "hello"
print(" ".join(l))

st = "((())){{stAsdas}Sd)"
arr = ''.join(c for c in st if c in "()[]")
print(arr)

# 문자열 정렬
st = "HelloWorld"
l = sorted(st)
print(l)

# split() 함수
st = "i wanna watch a movie"
l = st.split()
print(l)

# strip() 함수
# st = input()
# l = list(st)
# print(l)
# l = list(st.strip())
# print(l)
st = "tthello tt worldtt"
print(st.strip('t'))

# eval() 함수
exp = "1+2+3+4"
print(eval(exp))

# range() 함수
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(5, 10)))

# sort() 함수
l = [1, 6, 2, 3, 9, 10, 5]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

# insert() 함수
l = ['123', '456', '789']
l.insert(-1, 'xxx')
print(l)