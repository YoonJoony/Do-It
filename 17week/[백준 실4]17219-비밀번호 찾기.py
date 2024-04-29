# 첫째 줄에 저장된 사이트 주소의 수 N과 비밀번호를 찾으려는 사이트 주소의 수 M을 입력받습니다.
N, M = map(int, input().split())

# 사이트 주소와 비밀번호를 저장할 딕셔너리를 선언합니다.
passwords = {}

# 다음 N개의 줄에 걸쳐 사이트 주소와 비밀번호를 입력받아 딕셔너리에 저장합니다.
for _ in range(N):
    site, password = input().split()
    passwords[site] = password

# 다음 M개의 줄에 걸쳐 비밀번호를 찾고자 하는 사이트 주소를 입력받습니다.
# 해당 사이트 주소의 비밀번호를 딕셔너리에서 찾아 출력합니다.
for _ in range(M):
    site = input()
    print(passwords[site])
