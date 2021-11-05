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

def bfs(graph, start_node):
    visited, need_visit = list(), list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in need_visit:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
