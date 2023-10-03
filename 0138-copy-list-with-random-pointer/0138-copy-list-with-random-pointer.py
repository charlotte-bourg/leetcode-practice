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
        oldLst = []
        oldToNew = {}
        # traverse to end of existing linked list 
        while currOld:
            oldLst.append(currOld)
            currOld = currOld.next
        newLst = []
        prevNew = None
        # construct new linked list from back to front with just .next
        while oldLst: 
            currOld = oldLst.pop()
            currNew = Node(currOld.val, prevNew)
            oldToNew[currOld] = currNew
            newLst.append(currNew)
            prevNew = currNew
        newHead = currNew
        currOld = head
        # fill in .random
        while currNew:
            if currOld.random == None:
                currNew.random = None
            else: 
                currNew.random = oldToNew[currOld.random]
            currNew = currNew.next
            currOld = currOld.next
        return newHead
        
            