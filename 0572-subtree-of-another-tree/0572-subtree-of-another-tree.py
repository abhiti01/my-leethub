# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val == subRoot.val and isSameTree(root.left,subRoot.left) and isSameTree(root.right, subRoot.right):
                return True
            else:
                return False
        if root is None:
            return False
        if isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)