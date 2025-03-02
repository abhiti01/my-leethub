class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        dic={}
        ans=0
        while(r<len(s)):
            c = s[r]
            dic[c] = dic.get(c,0)+1
            cells = r-l+1
            cost = cells-max(dic.values())
            if cost>k:
                dic[s[l]]-=1
                l+=1
            else:
                ans=max(ans,r-l+1)
            r+=1
        return ans
                