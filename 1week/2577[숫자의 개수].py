#백준 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)

numbers = {
  "0": 0, "1": 0, "2": 0, "3": 0, "4": 0,
  "5": 0, "6": 0, "7": 0, "8": 0, "9": 0
}

for val in result:
    numbers[val] += 1

for val in numbers:
    print(numbers[val])