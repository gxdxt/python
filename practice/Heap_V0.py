# 최대값과 최소값을 빠르게 찾아야하는 우선순위 큐와 같은 자료구조
# 일반 배열에서는 최대값 최소값을 찾는 데에 O(n)이 소요된다.
# 힙에서는 O(log n)이 소요된다.

# 완전 이진 트리가 그 종류!

# 최대값을 구하기 위한 최대 힙
# 최소값을 구하기 위한 최소 힙

# Heap 은 보통 배열을 사용한다.
# Heap index 는 부모와 자식노드를 구하기 쉽다.
# 자식 노드 인덱스로 부모 노드 인덱스 -> 자식 노드 / 2
# 부모 노드 인덱스로 자식 노드 인덱스 -> 부모 노드 * 2 (왼쪽) & 부모 노드 * 2 + 1 (오른쪽)

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        # 1부터 시작하는 것이 위의 인덱스 구하기 쉬워서 배열의 첫 인덱스는 None
        self.heap_array.append(None)
        self.heap_array.append(data)

    # 삽입하는 데이터의 크기를 이전 노드와 비교하여 위치를 변경해야하는 지 확인하는 함수 >> True이면 위치 변경
    def move_up(self, inserted_idx):
        # 삽입하는 노드가 루트 노드일 경우에는 할 필요 없다.
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
            return True
        else:
            return False


    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        # 삽입하는 데이터가 루트 노드가 아닐 경우, 데이터 위치 변경의 코드들이 필요하다.

        # 지금 들어가는 데이터의 index 번호를 알아야 한다.
        inserted_idx = len(self.heap_array) - 1
        while self.move_up(inserted_idx):
            # 부모 노드의 idx 뽑기
            parent_idx = inserted_idx // 2 # /면 소수점까지 모두 나오고, //하면 몫 자연수만 나온다.
            # 두 자리를 변경한다.
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx] # swap
            inserted_idx = parent_idx
            # Q. 그럼 기존 parent_idx는 inserted_idx로 변경 안해줘도 되나?
            # A. 해당 idx 값은 실제 값이 아니라 자체적으로 부여한 임시 값이기 때문에 상관 없다.

        return True

    def move_down(self, poped_idx):
        left_idx = poped_idx * 2
        right_idx = poped_idx * 2 + 1
        # 0. 자식 노드가 없는 경우 -> 그냥 끝
        if left_idx >= len(self.heap_array):
            return False

        # 1. 자식 노드가 왼쪽만 있는 경우
        elif right_idx >= len(self.heap_array):
            # 왼쪽 자식 노드가 더 클 때, 해야할 일이 있다 > return True
            if self.heap_array[poped_idx] < self.heap_array[left_idx]:
                return True
            else:
                return False
        # 2. 자식 노드가 둘 다 있는 경우
        else:
            # 2 - 1. 자식 노드끼리 크기 비교
            if self.heap_array[left_idx] > self.heap_array[right_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_idx]:
                    return True
                else:
                    return False

    # Heap에서는 중간에 끼인 값을 삭제하는 경우는 없다.
    def pop(self):
        # 방어코드
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        # -1은 항상 마지막 데이터
        self.heap_array[1] = self.heap_array[-1]
        # 맨 끝 데이터 삭제
        del self.heap_array[-1]
        poped_idx = 1

        while self.move_down(poped_idx):
            left_idx = poped_idx * 2
            right_idx = poped_idx * 2 + 1

            if left_idx >= len(self.heap_array):
                return False

            # 1. 자식 노드가 왼쪽만 있는 경우
            elif right_idx >= len(self.heap_array):
                # 왼쪽 자식 노드가 더 클 때, 해야할 일이 있다 > return True
                if self.heap_array[poped_idx] < self.heap_array[left_idx]:
                    self.heap_array[poped_idx], self.heap_array[left_idx] = self.heap_array[left_idx], self.heap_array[poped_idx]
                    poped_idx = left_idx

            # 2. 자식 노드가 둘 다 있는 경우
            else:
                # 2 - 1. 자식 노드끼리 크기 비교
                if self.heap_array[left_idx] > self.heap_array[right_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_idx]:
                        self.heap_array[poped_idx], self.heap_array[left_idx] = self.heap_array[left_idx], self.heap_array[poped_idx]
                        poped_idx = left_idx
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_idx]:
                        self.heap_array[poped_idx], self.heap_array[right_idx] = self.heap_array[right_idx], self.heap_array[poped_idx]
                        poped_idx = right_idx


        return returned_data

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)

# Heap의 시간 복잡도는 최악의 상황에서 root -> leaf까지 탐색해야 한다. 그 후 삽입 혹은 삭제 할텐데,
# 이 때, 그 시간은 해당 힙의 depth만큼, 즉 log2 n 만큼 소요된다! O(log n)
