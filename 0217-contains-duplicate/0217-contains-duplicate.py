class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums=set()
        for i in range(len(nums)):
            if nums[i] in setNums:
                return True
            setNums.add(nums[i])