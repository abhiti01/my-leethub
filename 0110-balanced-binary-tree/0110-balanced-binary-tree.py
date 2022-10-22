# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if not root:
                return 0
            else:
                return 1+max(getHeight(root.left),getHeight(root.right))
        if not root:
            return True
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)
        if abs(leftHeight-rightHeight)>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
