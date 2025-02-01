# B050. 트리의 지름 - Baekjoon
# 어려운 문제 나중에 다시

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    distances = [-1] * (V + 1)  # 각 노드까지의 거리 저장
    distances[start] = 0
    farthest_node, max_distance = start, 0

    while queue:
        node = queue.popleft()
        for next_node, cost in graph[node]:
            if distances[next_node] == -1:  # 방문하지 않은 노드만 탐색
                distances[next_node] = distances[node] + cost
                queue.append(next_node)

                # 가장 먼 노드와 거리 갱신
                if distances[next_node] > max_distance:
                    max_distance = distances[next_node]
                    farthest_node = next_node

    return farthest_node, max_distance

# 입력 받기
V = int(input())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while data[idx] != -1:
        graph[node].append((data[idx], data[idx + 1]))
        idx += 2

# 첫 번째 BFS 수행 (아무 노드에서 가장 먼 노드 찾기)
farthest_node, _ = bfs(1)

# 두 번째 BFS 수행 (farthest_node에서 가장 먼 노드 찾기)
_, tree_diameter = bfs(farthest_node)

# 결과 출력
print(tree_diameter)
