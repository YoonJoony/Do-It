class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def add(data):
    node = head
    while node.right:
        node = node.right
    node.right = Node(data)
    node.right.left = node


node1 = Node(1)
head = node1
add(2)
add(3)

node = head
while node.right:
    print(node.data)
    node = node.right
print(node.data)
print()

while node.left:
    print(node)