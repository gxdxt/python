from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    # 인접 간선 정보들 모으기
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        # 해당 간선에 연결된 정점들 리스트를 미리 모두 집어 넣는다.
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))
        # 방향 그래프가 아니기 때문에, 둘 다 추가해 주어야 한다.
        # 일종의 초기화 코드

    connected_node = set(start_node)
    # 집합 데이터 타입으로 선언
    candidated_edge_list = adjacent_edges[start_node]
    # 선택된 노드에 대한 간선 정보들을 넣는다.

    # 위에 넣은 간선 정보들을 pop하려면, heapq 형태의 자료구조여야 한다.
    heapify(candidated_edge_list)

    # 후보군 간선 리스트가 없을 때 까지 반복문을 돌린다.
    while candidated_edge_list:
        weight, n1, n2 = heappop(candidated_edge_list)

        if n2 not in connected_node:
            connected_node.add(n2)
            mst.append((weight, n1, n2))
            # 첫 실행 시에, n1 -> n2 로 가는 간선을 선택했으니, 이제 n2를 시작으로 하는 최소 간선을 선택하게끔 데이터를 넣어주어야 한다.
            for edge in adjacent_edges[n2]:
                # edge에는 weight, n1, n2 튜플이 들어있으니, [2]는 n2(n2를 n1에 넣었으니까 n3 정도,,)를 의미한다.
                if edge[2] not in connected_node:
                    heappush(candidated_edge_list, edge)
                else:
                    print(edge[2] + '는 이미 연결된 노드입니다.')
        else:
            print(n2 + '는 이미 연결된 노드입니다.')

    return mst



myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

print(prim('A', myedges))