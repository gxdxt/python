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
        # 해당 노드를 찾았는지 여부 Flag
        searched = False
        self.current_node = self.head
        # 삭제 작업은 항상 parent node도 수정해줘야 하기에 선언
        self.parent = self.head

        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

        ## 여기부터 return되지 않았을 경우에 case를 나눠서 실행

        # Case 1 : Node가 Leaf Node일 경우,
        # 먼저 leaf node인지 판단,
        if self.current_node.left == None and self.current_node.right == None:
            # 삭제해야할 Node가 left인지, right인지도 판단해야한다. -> parent의 left를 None으로 만들 것인지, right를 None으로 만들 것인지 정해야 한다.
            if value < self.parent.vale:
                # 작을 경우는 left
                self.parent.left = None;
            else:
                # 클 경우는 right
                self.parent.right = None;
                # Memory 상에서도 삭제
                del self.current_node
            



#---------------------------------------------------잘못 작성한 코드
        """
        while value != self.current_node.value:
            # 해당 value가 있는 current_node로 이동
            if value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        # 전부 조회했는데 해당 Value에 대한 Node가 없는 경우

        # While 문에서 벗어나면 해당 value가 current_node인 상태

        # 삭제하는 노드가 leaf node일 경우
        if self.current_node.left == None and self.current_node.right == None:
            # 그냥 삭제
            self.current_node.value = None

        # 삭제하는 노드가 1개의 child node를 가지고 있을 경우
        elif self.current_node.left == None or self.current_node.right == None:
            # 해당 child node로 대체
            if self.current_node.left != None:
                replaceNode = self.current_node.left
                self.current_node.value = replaceNode.value
            else:
                replaceNode = self.current_node.right
                self.curent_node.value = replaceNode.value

        # 삭제하는 노드가 2개의 child nodes를 가지고 있을 경우
        elif self.current_node.left != None and self.current_node.right != None:
                # 삭제하는 노드의 left child node의 맨 우측 leaf node로 대체하는 경우
                replaceNode = self.current_node.left
                if replaceNode.right != None:
                    replaceNode = replaceNode.right
                        # 대체하려는 node가 right child node를 가진 경우
                            # right child node를 대체한 node 자리로 이동

                # 삭제하는 노드의 right child node의 맨 좌측 leaf node로 대체하는 경우우
                if replaceNode.left != None:
                    replaceNode = replaceNode.left
                        # 대체하려는 node가 left child node를 가진 경우
                            # left child node를 대체한 node 자리로 이동
                            """
