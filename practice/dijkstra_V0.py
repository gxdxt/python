import heapq

def dijkstra(graph, start):
    # region 기본 초기화 세팅 start

    distances = {node: float('inf') for node in graph}
    # graph 안에 있는 모든 node를 뽑아서 inf를 부여한다.

    distances[start] = 0
    # 첫 출발 vertex는 inf를 0으로 업데이트 한다.

    queue = []
    # 우선순위 큐로 사용할 list를 선언한다.

    heapq.heappush(queue, [distances[start], start])
    # 이게 아마 queue에 현재 해당되는 값을 우선순위 큐에 push하는 부분인 것 같다.
    # -> 초기값을 넣느라고 저렇게 쓴 것이다. 최초 시작 지점인 [0, 'A']를 넣은 것이다. (current_node, current_distance 세팅을 위해)
    # queue에 [거리, 노드] 형태로 값을 넣을 것이기 때문에 저렇게 세팅
    # 거리가 앞에 있는 이유는, 우선순위 큐의 기준이 '거리'이기 때문이다.


    # region 기본 초기화 세팅 end

    while queue:
        # queue에 값이 존재할 때까지 반복문 실행
        current_distance, current_node = heapq.heappop(queue)
        # heappop이기 때문에 가장 작은 distance의 값이 뽑아져서 current_node와 current_distance에 들어간다.

        # 우선순위 큐에 들어온 distance가 이미 배열(distances) 안에 있는 값보다 크면 반복문을 돌릴 필요도 없다.
        # -> skip
        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            # current_node에 있는(그래프 상으로 연결된) 값들이 모두 들어온다.
            # A의 경우 B, C, D 가 adjacent에 들어오게 된다.
            distance = current_distance + weight
            # 진정한 거리는 현재까지의 거리 + 현재 노드에서부터의 거리
            if distance < distances[adjacent]:
                # 더한 값이 최단 거리보다 작으면 업데이트
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances
# 시작 지점부터 각 vertex까지 최단거리를 출력하는 dijkstra 알고리즘 완성!

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(mygraph, 'A'))

# 최단 거리의 모습을 출력하는 다익스트라도 참고

def dijkstra2(graph, start, end):
    distances = {vertex: [float('inf'), start] for vertex in graph}

    distances[start] = [0, start]

    queue = 0

    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if distances[current_vertex] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = distances[current_vertex][0] + weight

            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances


