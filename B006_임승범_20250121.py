# B006. BFS와 DFS
from collections import defaultdict, deque

def dfs(graph, start, visited):
    visited[start] = True
    dfs_result.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = {node: False for node in graph}
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result


N, M, V = map(int, input().split())
graph = defaultdict(list) # 일반적인 dictionary와 달리 default value를 설정할 수 있다.

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

visited = {node: False for node in graph}
dfs_result = []

dfs(graph, V, visited)
print(' '.join(map(str, dfs_result)))

bfs_result = bfs(graph, V)
print(' '.join(map(str, bfs_result)))