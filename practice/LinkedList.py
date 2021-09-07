class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(2)
# 각각 독립적인 노드 2개를 생성 (next 값이 둘다 none이기 때문에)

# 이 둘을 잇기 위해서는 next를 추가하면 된다.
node1.next = node2
head = node1 # Linked List의 첫 번째 노드 선언


# 노드 추가 함수
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

for index in range(2, 10):
    add(index)

node1 = Node(1)
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else :
        node = node.next
node3.next = node.next
node.next = node3
while node.next:
    print(node.data)
    node = node.next
print(node.data)



