# B020. 숫자판 점프 - Baekjoon
# 생각해내기 까다로운 문제, 나중에 다시 풀기
# dfs 함수를 만들어내는 논리를 잘 생각해보기

def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    # 입력 처리
    board = [list(map(int, line.split())) for line in data]
    n, m = 5, 5  # 숫자판 크기
    
    # 이동 방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 고유한 숫자를 저장할 집합
    result = set()
    
    # DFS 함수
    def dfs(x, y, path):
        # 6자리 숫자가 완성되면 집합에 추가
        if len(path) == 6:
            result.add(path)
            return
        
        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx, ny, path + str(board[nx][ny]))
    
    # 모든 위치에서 DFS 시작
    for i in range(n):
        for j in range(m):
            dfs(i, j, str(board[i][j]))
    
    # 결과 출력
    print(len(result))
