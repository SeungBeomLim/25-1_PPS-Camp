# B016. Increasing Order Search Tree - Leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def in_order(node):
            if not node:
                return 
            
            in_order(node.left)
            
            node.left = None
            self.current.right = node
            self.current = node

            in_order(node.right)
        
        dummy = TreeNode(-1)
        self.current = dummy

        in_order(root)

        return dummy.right