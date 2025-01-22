# B017. Invert Binary Tree - Leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left # Python 에서 swap 할 때는 이렇게 한다!

        return root