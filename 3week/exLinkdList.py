class Node:
    def __init__(self, data, next=None):  # data만 입력 시 next 초기값은 0.
        self.data = data
        self.next = next  # 다음 데이터 주소 초기값 = None


# 노드 생성해보기
# node1 = Node(1)
# node2 = Node(3)
# # 1. Node 연결하기
# node1.next = node2
# # 가장 맨 앞 Node를 알기 위해 head 지정
# head = node1
#
# # node1을 통해 연결한 결과 확인
# print(node1.next.data)
# print(node2.data)


# 2. Node 뒤에 값(tail) 추가하기
# def add(data):
#     node = head  # 해당 노드 head 위치부터 돌리기 시작
#     while node.next:  # node의 next가 있을 경우만 반복
#         node = node.next  # 댜음 노드가 있는지 계속 반복
#     node.next = Node(data)  # 마지막 노드일 경우 뒤에 노드 추가
#
#
# node1 = Node(1)
# head = node1
#
# add(3)
# print(node1.data)
# print(node1.next.data)

# 3. 전체 노드 출력
def add(data):
    node = head  # 해당 노드 head 위치부터 돌리기 시작
    while node.next:  # node의 next가 있을 경우만 반복
        node = node.next  # 댜음 노드가 있는지 계속 반복
    node.next = Node(data)  # 마지막 노드일 경우 뒤에 노드 추가


node1 = Node(1)
head = node1
# 함수로 노드 추가
add(2)
add(3)
add(4)

node = head
while node.next:
    print(node.data)
    node = node.next  # 다음 노드가 있을 떄까지 반복
print(node.data) # 마지막 노드 출력
