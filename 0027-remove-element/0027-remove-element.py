class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        slow ptr for storing values that are not val, fast ptr for finding those values
        [0,1,2,2,3,0,4,2], val =2
        [0,1,3,2,2,0,4,2]
         sf
          sf
            sf
            s  f
            s   f
              s    f            
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                
        return slow
        '''
        
        slow =0
        fast=0
        while(fast<len(nums)):
            if nums[fast] !=val:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow+=1
            fast+=1
        return slow