class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index_total=0
        num_total=0
        
        for i in range(len(nums)):
            index_total+=i
            num_total += nums[i]
            
        return index_total+len(nums)-num_total