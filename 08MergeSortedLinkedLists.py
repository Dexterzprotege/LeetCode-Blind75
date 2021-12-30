# Question: https://leetcode.com/problems/merge-two-sorted-lists/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

# Verdict:
# Runtime: 32 ms, faster than 91.99% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.2 MB, less than 62.84% of Python3 online submissions for Merge Two Sorted Lists.
