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


