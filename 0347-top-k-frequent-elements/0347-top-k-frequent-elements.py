class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        from heapq import heappush,heappop
        h=[]
        output=[]
        for num in nums:
            dic[num] = dic.get(num,0)+1
        for key in dic:
            heappush(h, (dic[key],key))
            if len(h)>k:
                heappop(h)
        for (freq,num) in h:
            output.append(num)
        return output