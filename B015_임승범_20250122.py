# B015. 점프펌프 - Baekjoon

# bfs 풀이
from collections import deque

def count_reachable_stones(n, stones, start):
    visited = [False] * n  # 방문 여부를 저장
    queue = deque([start - 1])  # 시작 지점은 0 기반 인덱스
    
    visited[start - 1] = True  # 시작 지점을 방문 처리
    count = 1  # 시작 지점 포함
    
    while queue:
        current = queue.popleft()
        jump = stones[current]
        
        # 왼쪽으로 점프
        left = current - jump
        if 0 <= left < n and not visited[left]:
            visited[left] = True
            queue.append(left)
            count += 1
        
        # 오른쪽으로 점프
        right = current + jump
        if 0 <= right < n and not visited[right]:
            visited[right] = True
            queue.append(right)
            count += 1
    
    return count

# 입력 처리
n = int(input())
stones = list(map(int, input().split()))
start = int(input())

# 결과 출력
print(count_reachable_stones(n, stones, start))

# dfs 풀이
def dfs(current, n, stones, visited):
    visited[current] = True
    count = 1

    left = current - stones[current]
    if 0 <= left < n and not visited[left]:
        count += dfs(left, n, stones, visited)

    right = current + stones[current]
    if 0 <= right < n and not visited[right]:
        count += dfs(right, n, stones, visited)
    
    return count

n = int(input())
stones = list(map(int, input().split()))
start = int(input())

visited = [False] * n
result = dfs(start - 1, n, stones, visited)

print(result)