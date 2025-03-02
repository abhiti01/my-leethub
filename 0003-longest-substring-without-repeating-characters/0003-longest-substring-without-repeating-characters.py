class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        left = 0
        right =0
        windowLen=0
        charCounter={}
        maxLen=float('-inf')
        while left<=right and right<len(s):
            charCounter[s[right]] = charCounter.get(s[right],0)+1
            while charCounter[s[right]]>1:
                charCounter[s[left]] -=1
                left+=1
            windowLen = right-left+1
            maxLen = max(maxLen,windowLen)
            right+=1
        return maxLen