# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        sortedlist = dummy
        while l1 and l2:
            if l1.val < l2.val:
                sortedlist.next = l1
                l1 = l1.next
            else:
                sortedlist.next = l2
                l2 = l2.next
            sortedlist = sortedlist.next
        sortedlist.next = l1 or l2
        return dummy.next





