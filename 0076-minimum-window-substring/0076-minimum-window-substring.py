class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left =0
        right=0
        tFreq = collections.Counter(t)
        sFreq={}
        need = len(tFreq)
        have=0
        lenAns = float('inf')
        ans=[-1,-1]
        while(right<len(s)):
            sFreq[s[right]] = sFreq.get(s[right],0)+1
            if s[right] in tFreq and sFreq[s[right]] == tFreq[s[right]]:
                have+=1
            while have == need:
                if right-left+1<lenAns:
                    lenAns = right-left+1
                    ans=[left,right]
                sFreq[s[left]]-=1
                if s[left] in tFreq and sFreq[s[left]] < tFreq[s[left]]:
                    have-=1
                left+=1
            right+=1
        return s[ans[0]:ans[1]+1] if lenAns!=float("inf") else ""