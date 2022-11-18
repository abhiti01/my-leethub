class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxStreak = 0
        for num in nums:
            if num-1 in setNums:
                continue
            else:
                currentStreak =1
                while num+1 in setNums:
                    currentStreak+=1
                    num=num+1
                maxStreak = max(currentStreak,maxStreak)
        return maxStreak