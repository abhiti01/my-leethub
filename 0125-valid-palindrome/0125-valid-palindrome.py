class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for c in s:
            s1=s1+c.lower() if c.isalnum() else s1
        print(s1)
        left=0
        right = len(s1)-1
        while (left<right):
            if s1[left]!=s1[right]:
                return False
            left+=1
            right-=1
        return True