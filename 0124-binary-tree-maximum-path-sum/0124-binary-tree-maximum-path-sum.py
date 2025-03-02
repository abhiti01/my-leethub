# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root == None:
                return 0
            leftSum = max(helper(root.left),0)
            rightSum = max(helper(root.right),0)
            currentSum = leftSum + rightSum + root.val
            maxSum[0] = max(maxSum[0],currentSum)
            return max(leftSum+root.val,rightSum+root.val)
        maxSum = [float('-inf')]
        val = helper(root)
        return maxSum[0]
    
        
           