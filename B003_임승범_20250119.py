# B003. Sum of Left Leaves - Leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0

        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)

        return total
    

# DFS
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # 트리가 비어있는 경우

        stack = [root]  # 탐색을 위한 스택 초기화
        total = 0  # 왼쪽 잎 노드 값 합계

        while stack:
            node = stack.pop()  # 스택에서 노드 꺼내기

            # 왼쪽 자식이 있는 경우
            if node.left:
                # 왼쪽 자식이 잎 노드라면 값을 더함
                if not node.left.left and not node.left.right:
                    total += node.left.val
                else:
                    stack.append(node.left)  # 잎 노드가 아니면 스택에 추가

            # 오른쪽 자식이 있으면 스택에 추가
            if node.right:
                stack.append(node.right)

        return total


# BFS
from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # 트리가 비어있는 경우

        queue = deque([root])  # 탐색을 위한 큐 초기화
        total = 0  # 왼쪽 잎 노드 값 합계

        while queue:
            node = queue.popleft()  # 큐에서 노드 꺼내기

            # 왼쪽 자식이 있는 경우
            if node.left:
                # 왼쪽 자식이 잎 노드라면 값을 더함
                if not node.left.left and not node.left.right:
                    total += node.left.val
                else:
                    queue.append(node.left)  # 잎 노드가 아니면 큐에 추가

            # 오른쪽 자식이 있으면 큐에 추가
            if node.right:
                queue.append(node.right)

        return total
