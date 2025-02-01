# B049. 트리의 부모 찾기 - Baekjoon
# bfs 기본 개념 문제

import sys
from collections import deque

input = sys.stdin.readline

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if parents[child] == 0:  # 방문하지 않은 노드
                parents[child] = node  # 부모 설정
                queue.append(child)  # 큐에 추가

# 입력 받기
N = int(input())
graph = {i: [] for i in range(1, N + 1)}
parents = [0] * (N + 1)  # 부모 노드 저장 (1-based index)

# 트리 정보 입력받기
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 실행 (루트 노드는 1)
bfs(1)

# 결과 출력 (2번 노드부터 N번 노드까지)
for i in range(2, N + 1):
    print(parents[i])

