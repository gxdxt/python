# tree : node와 branch로 이루어진 데이터 구조

# node:
# root node:
# level:
# parent node:
# child node:
# leaf node:
# sibling (brother node):
# depth:

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)

    def delete(self, value):
        self.current_node = self.head
        while self.current_node:
            # 삭제하는 노드가 leaf node일 경우
            # 그냥 삭제

            # 삭제하는 노드가 1개의 child node를 가지고 있을 경우
            # 해당 child node로 대체

            # 삭제하는 노드가 2개의 child nodes를 가지고 있을 경우

                # 삭제하는 노드의 left child node의 맨 우측 leaf node로 대체하는 경우
                    # 대체하려는 node가 right child node를 가진 경우
                        # right child node를 대체한 node 자리로 이동

                # 삭제하는 노드의 right child node의 맨 좌측 leaf node로 대체하는 경우우
                    # 대체하려는 node가 left child node를 가진 경우
                        # left child node를 대체한 node 자리로 이동
    