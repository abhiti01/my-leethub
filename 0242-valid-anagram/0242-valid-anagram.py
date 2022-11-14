class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
#         for char in s:
#             if char not in dic:
#                 dic[char] = 1
#             else:
#                 dic[char] += 1
        
#         for char in t:
#             if char not in dic:
#                 return False
#             else:
#                 dic[char] -= 1
        
#         for val in dic.values():
#             if val != 0:
#                 return False
        
#         return True

        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0)+1
        for i in range(len(t)):
            dic[t[i]]=dic.get(t[i],0)-1
            if dic[t[i]]<0:
                return False
        return True
        