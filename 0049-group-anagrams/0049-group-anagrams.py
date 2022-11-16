class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic ={}
        for str in strs:
            if "".join(sorted(str)) not in dic:
                dic["".join(sorted(str))] = [str]
            else:
                dic["".join(sorted(str))].append(str)
        return dic.values()