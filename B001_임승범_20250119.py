# B001. 바이러스 - Baekjoon
# 그래프 문제이고 DFS 혹은 BFS를 통해 해결하면 된다.
# DFS는 재귀함수 혹은 스택을 사용하고 경로 탐색이나 분기 한정 문제에 적합하다.
# BFS는 큐를 사용하고 최단 거리 문제에 적합하다.   

# DFS Code
def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
        

computer = int(input())
connection = int(input())

graph = {i: [] for i in range(1, computer + 1)}

for _ in range(connection):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer+1)
dfs(graph, 1, visited)

print(visited.count(True) - 1)

# BFS Code
from collections import deque

def bfs(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return visited

# 입력 처리
n = int(input())  # 컴퓨터 수
m = int(input())  # 네트워크 연결 수
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 수행
visited = bfs(graph, 1)

# 결과 출력 (1번 컴퓨터를 제외하고 연결된 컴퓨터 수 계산)
print(visited.count(True) - 1)
