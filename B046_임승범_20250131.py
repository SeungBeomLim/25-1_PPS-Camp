# B046. Flood Fill - LeetCode

# dfs 풀이
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or image[x][y] != original_color:
                return
            
            image[x][y] = color

            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x, y-1)
        
        dfs(sr, sc)
        return image
    
    
# bfs 풀이
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        if original_color == color:
            return image  # 이미 같은 색이면 변경할 필요 없음
        
        queue = deque([(sr, sc)])
        image[sr][sc] = color  # 첫 픽셀 변경
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우 이동
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        
        return image