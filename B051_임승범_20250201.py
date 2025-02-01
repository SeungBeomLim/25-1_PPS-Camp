# B051. Binary Tree Paths - LeetCode

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return
            
            # 현재 노드의 값을 path에 추가
            path += str(node.val)
            
            # 만약 leaf 노드라면 결과 리스트에 경로 추가
            if not node.left and not node.right:
                result.append(path)
            else:
                # 하위 노드 탐색 (좌/우)
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)
        
        result = []
        dfs(root, "")
        return result
