class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #  l                     r          maxL = 0, maxR=1
#         other solution
        # maxLeft=0
        # maxRight=0
        # w=0
        # left=0
        # right = len(height)-1
        # while(left<right):
        #     if height[left]<height[right]:
        #         if height[left]>=maxLeft:
        #             maxLeft = height[left]
        #         else:
        #             w+=maxLeft-height[left]
        #         left+=1
        #     else:
        #         if height[right]>=maxRight:
        #             maxRight=height[right]
        #         else:
        #             w+=maxRight-height[right]
        #         right-=1
        # return w
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
