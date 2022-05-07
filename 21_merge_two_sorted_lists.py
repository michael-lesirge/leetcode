# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        set next node to min(list1, list2)
        if left or right is not done then add the entire rest of the list to end
        does not keep list1 and list2 intact
        
        None is falsy
        """
        dummy_head = ListNode()
        current = dummy_head
        
        while (list1 and list2):
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy_head.next
