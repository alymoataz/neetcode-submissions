# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def getheight(root):
            if not root:
                return 0
            return 1+max(getheight(root.left),getheight(root.right))
        return math.fabs(getheight(root.left)-getheight(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        