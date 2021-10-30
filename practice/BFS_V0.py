# 파이썬에서 제공하는 딕셔너리와 리스트 자료 구조를 통해 그래프를 구현할 수 있다.

# 각각의 노드들로 'Key'를 만든다.
# 각 'Key' 안에 인접 접점을 'Value'로 넣는다.


# 딕셔너리 객체 생성
graph = dict()

# 각각의 노드들을 'Key'값으로 추가 / Value 추가 (순서는 상관이 없다.)
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# 자료구조 queue를 활용한다.
def bfs(graph, start_node):
    visited, need_visit = list(), list()
    # queue를 사용해도 되지만, list에서 제공하는 메소드들로도 충분히 구현이 가능하다.

    # 비순환 그래프의 일종이기에 트리와 비슷한 느낌
    # 가장 먼저 시작할 노드를 넣는다.
    need_visit.append(start_node)

    # 1턴 시작 (턴들이 반복되니, while 구문을 사용한다.)
    while need_visit: # 방문해야 하는 노드가 더 이상 존재하지 않는다면, 해당 그래프를 모두 순회한 것으로 판단한다.

        # 순서
        # need_visit queue에 있는 첫 번째 데이터를 꺼낸다 (큐 니까)
        node = need_visit.pop(0) # 안에 index를 붙이지 않으면, 맨 뒤의 값이 pop 된다.
        # visited queue에 있는 지 확인한다.
        if node not in visited:
            # 꺼낸 데이터를 visited에 넣는다.
            visited.append(node)
            # 꺼낸 데이터의 value들을 순서대로 넣는다.
            need_visit.extend(graph[node]) # graph[node] 안에 있는 값을 need_visit 뒤로 확장한다.
    return visited # 방문된 노드가 순서대로 정리되어 있을 것이다.

    # 시간 복잡도
    # V = 노드의 수 (Vortex)
    # E = 간선의 수 (Edge)
    # while 문이 V+E 만큼 돌기 때문에
    # O(V+E)



    # 1턴 끝

        # 2턴 시작

        # need_visit에서 데이터 꺼낸다.
        # visited queue에 있는 지 확인한다.
        # 꺼낸 데이터를 visited에 넣는다.
        # 꺼낸 데이터의 value들을 뒤에 붙여 넣는다.

        # 2턴 끝

        # 3턴 시작

        # need_visit에서 데이터를 꺼낸다.
        # visited queue에 있는 지 확인한다.
        # 있으면 턴 끝

        # 3턴 끝





