# B004. Symmetric tree - Leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:   # 둘다 None인 경우
                return True
            if not t1 or not t2:    # 둘 중 하나만 None인 경우
                return False
            return (t1.val == t2.val and    # 둘의 값이 같고, root.left.left == root.right.right and root.left.rigth == root.right.left
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )

        return isMirror(root.left, root.right)