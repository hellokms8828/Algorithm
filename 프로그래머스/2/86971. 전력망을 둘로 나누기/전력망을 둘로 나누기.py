from collections import defaultdict, deque

def bfs(graph, start):
    visited = [start]
    q = deque([start])
    n = 1

    while q:
        node = q.popleft()

        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.append(adjacent)
                q.append(adjacent)
                n += 1

    return n


def solution(n, edges):
    answer = -1
    
    arr = []

    for edge1 in edges:
        graph = defaultdict(list)
        x, y = edge1
        for edge2 in edges:
            if edge1 == edge2:
                continue
            a, b = edge2
            graph[a].append(b)
            graph[b].append(a)

        n1 = bfs(graph, x)
        n2 = bfs(graph, y)

        arr.append(abs(n1 - n2))

    answer = min(arr)

    return answer
