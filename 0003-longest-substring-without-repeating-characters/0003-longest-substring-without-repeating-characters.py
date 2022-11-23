class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left=0
        right=0
        setChars=set()
        while (right<len(s)):
            while(s[right] in setChars):
                setChars.remove(s[left])
                left+=1
            setChars.add(s[right])
            maxLength = max(maxLength,right-left+1)
            right+=1
            
        return maxLength