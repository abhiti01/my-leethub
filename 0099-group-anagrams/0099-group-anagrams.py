class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic ={}
        for word in strs:
            if "".join(sorted(word)) not in dic:
                dic["".join(sorted(word))] = [word]
            else:
                dic["".join(sorted(word))].append(word)
        return list(dic.values())
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     ans: DefaultDict[int, List[str]] = collections.defaultdict(list)
    #     for s in strs:
    #         count = [0] * 26
    #         for c in s:
    #             count[ord(c) - ord("a")] += 1
    #         ans[tuple(count)].append(s)
    #     return ans.values()
# Time Complexity: 
# O(NK), where 
# N is the length of strs, and 
# K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
# Space Complexity: 
# O(NK), the total information content stored in ans.