class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(2)
# 각각 독립적인 노드 2개를 생성 (next 값이 둘다 none이기 때문에)

# 이 둘을 잇기 위해서는 next를 추가하면 된다.
node1.next = node2
