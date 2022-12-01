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
    #         other solution
        # lastSeen = {}
        # start = 0
        # length = 0
        # maxLength = 0
        # i=0
        # while i<len(s):
        #     if s[i] in lastSeen and start<=lastSeen[s[i]]:
        #         start = lastSeen[s[i]]+1
        #         lastSeen[s[i]] = i
        #     else:
        #         lastSeen[s[i]] = i   
        #     print(s[start:i+1])
        #     length = i-start+1
        #     maxLength = max(length,maxLength)
        #     i+=1
        # return maxLength