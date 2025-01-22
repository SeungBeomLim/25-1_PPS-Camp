# B012. 이진 검색 트리 - Baekjoon

import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

def postorder(tree):
    if not tree:  # 트리가 비어 있는 경우 종료
        return

    mid = tree[0]  # 루트 노드
    left_subtree, right_subtree = [], []

    # 서브트리를 나누는 로직
    for i in range(1, len(tree)):
        if tree[i] > mid:  # 오른쪽 서브트리가 시작하는 지점
            left_subtree = tree[1:i]
            right_subtree = tree[i:]
            break
    else:
        # 오른쪽 서브트리가 없는 경우
        left_subtree = tree[1:]

    # 재귀적으로 후위 순회
    postorder(left_subtree)
    postorder(right_subtree)
    print(mid)  # 루트를 출력

# 입력 처리
input = sys.stdin.read
preorder = list(map(int, input().split()))

# 후위 순회 호출
postorder(preorder)
