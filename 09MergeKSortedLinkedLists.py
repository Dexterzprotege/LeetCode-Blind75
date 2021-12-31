# Question: https://leetcode.com/problems/merge-k-sorted-lists/

# Time Complexities: (Space is O(1) if in-place and O(N) if extra)
# 4. Heap Solution -> O(NLogK)
# 3. Divide and Conquer Solution -> O(NLogK)
# 2. Simple (Add to one list and mergeSort) -> O(NLogN)
# 1. Simple (Two lists at a time merge) -> O(NK)

# ------------------------------------------------------------------------------------------------------------------------------------------- #

# Solution4: O(nlogk) -> Insert every first element into Heap, pop and then go on unitl list is empty
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from heapq import heappush, heappop
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while heap:
            val, i = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next

# Verdict:
# Runtime: 92 ms, faster than 94.40% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.8 MB, less than 81.34% of Python3 online submissions for Merge k Sorted Lists.

# ------------------------------------------------------------------------------------------------------------------------------------------- #

# Solution3: O(nlogk) -> Divide and Conquer technique, split in the same lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        tail = head = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        
        if not k:   return None
        if k == 1:  return lists[0]
        
        mid = k // 2
        left = self.mergeKLists(lists[0:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(left, right)

# Verdict:
# Runtime: 129 ms, faster than 34.42% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.7 MB, less than 81.34% of Python3 online submissions for Merge k Sorted Lists.

# ------------------------------------------------------------------------------------------------------------------------------------------- #

# Solution2: O(nlogn) -> Merge all into single list, apply mergeSort
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(left, right):
            head = ListNode(0)
            tail = head
            while left and right:
                if left.val > right.val:
                    tail.next = right
                    right = right.next
                else:
                    tail.next = left
                    left = left.next
                tail = tail.next
            if left:
                tail.next = left
            if right:
                tail.next = right
            return head.next
        def getMiddle(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow;
        def mergeSort(head):
            if head is None or head.next is None:
                return head
            middle = getMiddle(head)
            left, right = head, middle.next
            middle.next = None
            left = mergeSort(left)
            right = mergeSort(right)
            return mergeLists(left, right)

        Starter = ListNode(0)
        curr = Starter
        head = curr
        for i in lists:
            while i is not None:
                curr.next = i
                i = i.next
                curr = curr.next
        head = mergeSort(head.next)
        return head

# Verdict:
# Runtime: 224 ms, faster than 15.03% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.7 MB, less than 92.65% of Python3 online submissions for Merge k Sorted Lists.

# ------------------------------------------------------------------------------------------------------------------------------------------- #

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

# ------------------------------------------------------------------------------------------------------------------------------------------- #
