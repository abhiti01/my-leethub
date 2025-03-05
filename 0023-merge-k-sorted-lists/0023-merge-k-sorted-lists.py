# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        from heapq import heappush,heappop
        h=[]
        for i in range(0,len(lists)):
            if lists[i]:
                heappush(h,(lists[i].val,i))
                lists[i] = lists[i].next 
        
        ans = curr=ListNode(0)
        while h:
            value,listNo = heappop(h)
            ans.next = ListNode(value)
            if lists[listNo]:
                heappush(h,(lists[listNo].val,listNo))
                lists[listNo] = lists[listNo].next
            ans = ans.next
            
        print(ans)
        return curr.next