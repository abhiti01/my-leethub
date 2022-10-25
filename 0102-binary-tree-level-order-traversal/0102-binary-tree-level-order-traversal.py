# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        thisLevel =[root]
        output=[]
        while thisLevel and root:
            thisLevelNodes=[]
            nextLevel=[]
            for node in thisLevel:
                thisLevelNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            output.append(thisLevelNodes)
            thisLevel = nextLevel
            
        return output