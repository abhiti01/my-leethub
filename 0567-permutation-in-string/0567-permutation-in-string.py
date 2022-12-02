class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = collections.Counter(s1)
        left=0
        right=0
        s2Freq={}
        while(right<len(s2)):
            s2Freq[s2[right]] = s2Freq.get(s2[right],0)+1
            if right-left+1>len(s1):
                if s2Freq[s2[left]]==1:
                    s2Freq.pop(s2[left])
                else:
                    s2Freq[s2[left]]-=1
                left+=1
            if s2Freq == s1Freq:
                return True
            right+=1
        return False