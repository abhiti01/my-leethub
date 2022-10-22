# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter =0
        def longestPath(root):
            nonlocal diameter
            if not root:
                return 0
            l = longestPath(root.left)
            r = longestPath(root.right)
            diameter = max(diameter,l+r)
            return 1+max(l,r)
        longestPath(root)
        return diameter

