# B019. 적록색약 - Baekjoon
# 어려운 문제 나중에 다시 풀기!

import sys
sys.setrecursionlimit(10**6)

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 탐색 함수
def dfs(x, y, color, grid, visited, is_colorblind):
    visited[x][y] = True
    n = len(grid)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # 적록색약인 경우 R과 G를 같은 색으로 간주
            if is_colorblind:
                if grid[nx][ny] in ("R", "G") and color in ("R", "G"):
                    dfs(nx, ny, color, grid, visited, is_colorblind)
                elif grid[nx][ny] == color:
                    dfs(nx, ny, color, grid, visited, is_colorblind)
            # 일반인의 경우
            else:
                if grid[nx][ny] == color:
                    dfs(nx, ny, color, grid, visited, is_colorblind)

# 구역 수 계산 함수
def count_regions(grid, is_colorblind):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    region_count = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, grid[i][j], grid, visited, is_colorblind)
                region_count += 1
    
    return region_count

# 입력 처리
n = int(input())
grid = [input().strip() for _ in range(n)]

# 일반인의 구역 수 계산
normal_regions = count_regions(grid, is_colorblind=False)

# 적록색약의 구역 수 계산
colorblind_regions = count_regions(grid, is_colorblind=True)

# 결과 출력
print(normal_regions, colorblind_regions)
