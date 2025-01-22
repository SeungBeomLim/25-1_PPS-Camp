# B018. Path Sum - Leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val)
        )
    

# bfs
from collections import deque

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        # 큐 초기화: 노드와 남은 합을 저장
        queue = deque([(root, targetSum)])
        
        while queue:
            node, current_sum = queue.popleft()
            
            # 리프 노드일 때, 남은 합이 노드 값과 같으면 True 반환
            if not node.left and not node.right and current_sum == node.val:
                return True
            
            # 왼쪽 자식 추가
            if node.left:
                queue.append((node.left, current_sum - node.val))
            
            # 오른쪽 자식 추가
            if node.right:
                queue.append((node.right, current_sum - node.val))
        
        return False