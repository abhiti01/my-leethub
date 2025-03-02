class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = collections.Counter(t)
        need = len(tCounter)
        have=0
        left=0
        right=0
        lenAns = float('inf')
        ans=[-1,-1]
        sCounter = {}
        while right<len(s):
            sCounter[s[right]] = sCounter.get(s[right],0)+1
            if s[right] in tCounter and sCounter[s[right]] == tCounter[s[right]]:
                have+=1
            while have == need:
                if right - left +1 < lenAns:
                    lenAns = right-left+1
                    ans[0],ans[1]= left,right
                sCounter[s[left]] -=1
                if s[left] in tCounter and sCounter[s[left]]<tCounter[s[left]]:
                    have-=1
                left+=1
            right+=1
        return s[ans[0]:ans[1]+1] if lenAns!=float("inf") else ""