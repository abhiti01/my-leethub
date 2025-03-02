# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root,float('-inf'),float('inf'))
    
    def validateBST(self, root, minimum, maximum):
        if root == None:
            return True
        elif root.val>minimum and root.val<maximum:
            return self.validateBST(root.left,minimum,root.val) and self.validateBST(root.right,root.val,maximum)
        else: 
            return False