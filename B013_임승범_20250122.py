# B013. 물통 - Baekjoon

from collections import deque

A, B, C = map(int, input().split())

buckets = deque([(0, 0, C)])
visited = set()
result = set()

while buckets:
    a, b, c = buckets.popleft()

    if (a, b, c) in visited:
        continue
    visited.add((a, b, c))

    if a == 0:
        result.add(c)

    # 물 이동 가능한 모든 경우 탐색 (완전탐색)
    
    # A -> B
    move = min(a, B - b)
    buckets.append((a - move, b + move, c))

    # A -> C
    move = min(a, C - c)
    buckets.append((a - move, b, c + move))

    # B -> A
    move = min(b, A - a)
    buckets.append((a + move, b - move, c))

    # B -> C
    move = min(b, C - c)
    buckets.append((a, b - move, c + move))

    # C -> A
    move = min(c, A - a)
    buckets.append((a + move, b, c - move))

    # C -> B
    move = min(c, B - b)
    buckets.append((a, b + move, c - move))

# 결과 출력
print(" ".join(map(str, sorted(result))))