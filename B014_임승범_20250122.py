# B014. 섬의 개수 - Baekjoon
# 나중에 다시 풀기. 어려운 문제.

# BFS 풀이
import sys
from collections import deque

input = sys.stdin.read
data = input().strip().split("\n")

def bfs(x, y, w, h, grid, visited):
    # 8방향 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_islands(w, h, grid):
    visited = [[False] * w for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                # 새 섬 발견
                bfs(i, j, w, h, grid, visited)
                count += 1
    
    return count

# 입력 처리 및 결과 계산
results = []
i = 0
while i < len(data):
    w, h = map(int, data[i].split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int, data[i + j + 1].split())) for j in range(h)]
    results.append(count_islands(w, h, grid))
    i += h + 1

# 결과 출력
print("\n".join(map(str, results)))

# DFS 풀이
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

def dfs(x, y, w, h, grid, visited):
    # 8방향 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    visited[x][y] = True
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny, w, h, grid, visited)

def count_islands(w, h, grid):
    visited = [[False] * w for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                # 새 섬 발견
                dfs(i, j, w, h, grid, visited)
                count += 1
    
    return count

# 입력 처리 및 결과 계산
def solve():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    results = []
    i = 0
    while i < len(data):
        w, h = map(int, data[i].split())
        if w == 0 and h == 0:
            break
        grid = [list(map(int, data[i + j + 1].split())) for j in range(h)]
        results.append(count_islands(w, h, grid))
        i += h + 1

    # 결과 출력
    print("\n".join(map(str, results)))

