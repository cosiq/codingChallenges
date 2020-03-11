# Write a program to find the node at which the intersection of two singly linked lists begins.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

	def getIntersectionNode(self, headA, headB):
		if not (headA and headB): return None
        p1, p2, s1, s2 = headA, headB, 0, 0
        while(p1 != p2):
            if not (s1 or p1.next): s1, p1 = 1, headB
            else: p1 = p1.next
            if not (s2 or p2.next): s2, p2 = 1, headA
            else: p2 = p2.next
        return p1

    def anotherGetIntersection(self, headA, headB):
    	lst = set()
        while headA:
            lst.add(headA)
            headA = headA.next
        while headB:
            if headB in lst: return headB
            headB = headB.next