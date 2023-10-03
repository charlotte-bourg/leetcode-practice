"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import deque
# dictionary where keys are old node and vals are new node 
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        currOld = head
        oldToNew = {}
        preNewHead = Node(0, None, None)
        prevNew = preNewHead
        # construct new list with just .next
        while currOld:
            currNew = Node(currOld.val, None, None)
            oldToNew[currOld] = currNew
            currOld = currOld.next
            prevNew.next = currNew
            prevNew = currNew
        currNew = preNewHead.next
        currOld = head
        # fill in .random
        while currNew:
            if currOld.random == None:
                currNew.random = None
            else: 
                currNew.random = oldToNew[currOld.random]
            currNew = currNew.next
            currOld = currOld.next
        return preNewHead.next
        
            