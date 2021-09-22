
# 각각의 노드들이 연결되면서 결국 Linked List라는 구조가 생성되는 것이다. 이렇게 안에 들어있는 값은 다르지만, 그 형태 및 구조는 동일한 'Node'라는 것을 정의한 부분
# 즉, Node라는 값을 찍어낼 '거푸집'을 만든 것.
class Node:

    # __init__의 역할은 초기값을 선언하는 것이다.
    # Node가 호출될 때 항상 자동으로 실행되는 함수라고 생각하면 되는 것 같다.
    # 물론, setValue(self, data, prev, next)라는 함수를 만들고, 해당 클래스를 호출할 때 마다 setValue 함수도 호출해줘도 된다.
    # 근데 굳이?
    def __init__(self, data, prev=None, next=None):
        # self의 의미는 각각 인스턴스에서 활용하게 되는 부분이다.
        # 이 객체에서는 인스턴스를 위한 틀을 만들어 주는 것이다.
        # 여기서 지정한 self 값은 해당 객체가 인스턴스가 될 때 해당 인스턴스를 의미하는 인자가 된다.
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgnt:
    def __init__(self, data):
        self.head = Node(data)
        # 아마 최초의 시작에는 노드가 한 개뿐이니까, 그게 곧 머리이자 꼬리인 것.
        self.tail = self.head

    def insert(self, data):
        # 해당 노드에 아무 데이터가 존재하지 않을 때 방어코드
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            # 마지막 노드까지 넘어가기
            # tail을 바로 찾으면 안되나?
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        if node.data == data:
            return node
        else:
            node = node.next

    def search_from_tail(self, data):
        if self.node == None:
            return False

        node = self.tail
        if node.data == data:
            return node
        else:
            node = node.prev

    def insert_before(self, target, data):
        if self.head == None:
            self.node = Node(data)
            return True
        # 여기서 return Node(data)해도 되려나?
        else:

            node = self.head
            while node.data != target:
                # while에 조건문이 참이면 들어온다.
                node = node.next
                if node == None:
                    # 끝까지 돌았는데, 해당 타겟 값이 없으면 return False
                return False
            # data를 담은 새로운 노드 생성
            new = Node(data)

            # Insert 전의 현재 노드 전 데이터를 임시 변수에 저장
            temp = node.prev

            # 현재 노드 전 데이터를 삽입하려는 데이터로 변경
            node.prev = new

            # 기존 'prev' 데이터의 다음 데이터를 삽입하려는 데이터로 변경
            temp.next = new

            # 삽입하려는 데이터의 'prev' 데이터를 임시 저장한 이전의 데이터로 저장
            new.prev = temp

            # 삽입하려는 데이터의 'next' 데이터를 현재 노드 데이터로 저장
            new.next = node
            return True

    def insert_after(self, target, data):

