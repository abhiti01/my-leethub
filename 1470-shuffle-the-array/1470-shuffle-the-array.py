class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left=0
        ret=[]
        while(left<n):
            right=left+n
            ret.append(nums[left])
            ret.append(nums[right])
            left+=1
        return ret