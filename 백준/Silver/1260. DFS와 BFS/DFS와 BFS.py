from collections import deque, defaultdict

# 입력 받기
n, e, startnode = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

# 인접 리스트 생성
graph = defaultdict(list)
for fromnode, tonode in edges:
    graph[fromnode].append(tonode)
    graph[tonode].append(fromnode)  # 무방향 그래프의 경우

# 인접 리스트 정렬
for node in graph:
    graph[node].sort()

dfsvisited = [False] * (n + 1)
bfsvisited = [False] * (n + 1)

def dfs(startn):
    dfsvisited[startn] = True
    print(startn, end=" ")
    for nextnode in graph[startn]:
        if not dfsvisited[nextnode]:
            dfs(nextnode)

def bfs(startn):
    queue = deque([startn])
    bfsvisited[startn] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for nextnode in graph[node]:
            if not bfsvisited[nextnode]:
                queue.append(nextnode)
                bfsvisited[nextnode] = True

dfs(startnode)
print()
bfs(startnode)
