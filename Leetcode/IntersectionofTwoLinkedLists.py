# Write a program to find the node at which the intersection of two singly linked lists begins.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

	def getIntersectionNode(self, headA, headB):
		if not (headA and headB): return None
        currA, currB = headA, headB
        is_secondA, is_secondB = 0, 0
        while(currA != currB):
            if not (is_secondA or currA.next):
                is_secondA = 1
                currA = headB
            else: currA = currA.next
            if not (is_secondB or currB.next):
                is_secondB = 1
                currB = headA
            else: currB = currB.next
        return currA