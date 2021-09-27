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