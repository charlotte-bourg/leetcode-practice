# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def llToNum(self, curr):
        num = ""
        while curr.next: 
            num = str(curr.val) + num 
            curr = curr.next
        num = str(curr.val) + num 
        return int(num)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumString = str(self.llToNum(l1) + self.llToNum(l2))
        nextNode = None
        for char in sumString:
            curr = ListNode(val = char, next = nextNode)
            nextNode = curr
        return curr


    
        