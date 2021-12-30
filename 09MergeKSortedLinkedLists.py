# Question: https://leetcode.com/problems/merge-k-sorted-lists/

# Solution1: O(n*k) -> Merge two lists at a time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            Starter = ListNode(0)
            curr = Starter

            while list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    temp = list1
                    curr.next = temp
                    list1 = list1.next
                    temp.next = None
                else:
                    temp = list2
                    curr.next = temp
                    list2 = list2.next
                    temp.next = None
                curr = curr.next
            if list1 is None:
                curr.next = list2
            else:
                curr.next = list1

            return Starter.next
        
        if not lists:
            return None
        list1 = lists[0]
        for i in range(1, len(lists)):
            list2 = lists[i]
            list1 = mergeTwoLists(list1, list2)
        return list1

# Verdict:
# Runtime: 5788 ms, faster than 5.02% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.7 MB, less than 81.43% of Python3 online submissions for Merge k Sorted Lists.
