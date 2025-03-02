class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        maxL = height[0]
        maxR = height[len(height)-1]
        left=0
        right=len(height)-1
        while(left<right):
            if maxL<maxR:
                left+=1
                maxL = max(maxL,height[left])
                res+=maxL - height[left]
                
            else:
                right-=1
                maxR = max(maxR,height[right])
                res+=maxR - height[right]
                
        return res