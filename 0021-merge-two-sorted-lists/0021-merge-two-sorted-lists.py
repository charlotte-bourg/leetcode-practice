# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1Curr = list1
        l2Curr = list2
        if not l1Curr:
            return l2Curr
        if not l2Curr:
            return l1Curr
        if l1Curr.val < l2Curr.val:
            mergeHead = l1Curr
            l1Curr = l1Curr.next
        else:
            mergeHead = l2Curr
            l2Curr = l2Curr.next
        mergeCurr = mergeHead
        while l1Curr or l2Curr:
            if not l1Curr:
                mergeCurr.next = l2Curr
                l2Curr = l2Curr.next
            elif not l2Curr:
                mergeCurr.next = l1Curr
                l1Curr = l1Curr.next
            elif l1Curr.val < l2Curr.val:
                mergeCurr.next = l1Curr
                l1Curr = l1Curr.next
            else:
                mergeCurr.next = l2Curr
                l2Curr = l2Curr.next
            mergeCurr = mergeCurr.next
        return mergeHead
            