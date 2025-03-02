# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res=[]
        q.append(root)
        while q:
            level=[]
            qLen = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                level = level[::-1] if len(res)%2 else level
                res.append(level)
                
        return (res)