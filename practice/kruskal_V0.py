parent = dict()
rank = dict()
# 각각의 노드를 넣으면 부모 노드를 뱉는
# 각각의 노드를 넣으면 랭크를 뱉는

# 'root node' 찾는 함수
def find(node):
    # path compression 기법 사용 -> 중간에 있는 node들도 모두 root 노드로 붙여준다. / root node를 찾는 시간 복잡도를 낮춰준다.
    if parent[node] != node:
        # 자기 자신이 root node가 아니라면 들어온다.
        parent[node] = find(parent[node])
    return parent[node]

#
def union(node_v, node_u):
    # 2가지 조건에 따라 합쳐진다.
    # 각각의 노드의 root node를 알아낸다.
    root1 = find(node_v)
    root2 = find(node_u)
    # 1. 각각의 집합의 root node가 rank 값이 다를 때,
    # union by rank 기법
    if rank[root1] > rank[root2]:
        # 큰 쪽을 작은 쪽으로 연결해야 한다.
        parent[root2] = root1
    else:
        parent[root1] = root2
        # 2. 각각의 집합의 root node가 rank 값이 같을 떄,
        if rank[root1] == rank[root2]:
            rank[root2] += 1 # 하나의 랭크를 1 올린다.

# 초기화 함수
def make_set(node):
    # 모든 노드를 각각의 집합으로 만들어야 한다.
    parent[node] = node
    # 각각의 노드가 개별적으로 존재하기 때문에, 자기 자신이 곧 부모 노드가 된다.
    rank[node] = 0
    # 랭크 역시 0으로 초기화 한다.



mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'B', 'C'),

    ]
}

def kruskal(graph):
    mst = list()
    # 초기화
    # 각각의 노드를 개별 집합으로 이루어지도록 초기화
    for node in graph['vertices']:
        make_set(node)



    # 간선 weight 기반 sort
    edges = graph['edges']
    edges.sort()


    # 사이클 없는 간선만 연결
    for edge in edges:
        weight, node_v, node_u = edge
        # edge를 mst에 넣을지 말지 find라는 함수를 생성해서 확인하도록
        if find(node_v) !=  find(node_u):
            # 각각의 노드의 root노드가 다른지만 확인하면 된다.
            # 같으면 동일한 간선 안에 위치하기 떄문에, 사이클이 생기게 된다.
            # 다르다면 하나의 집합으로 합쳐져야 한다.
            union(node_v, node_u)
            mst.append(edge)
    return mst