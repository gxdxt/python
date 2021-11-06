def dfs(graph, start):
    visited, need_visit = list(), list()
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited