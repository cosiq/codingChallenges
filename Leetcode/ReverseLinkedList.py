# Reverse a singly linked list.
# Example:
#	 Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
#	 Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def recReverseList(head: ListNode):
	if head is None or head.next is None: return head
	res = recReverseList(head.next)
    head.next.next, head.next = head, None
	return res

# Time: O(N)
# Space: O(N)

def iterReverseList(head: ListNode):
	prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev,curr ,curr.next
    return prev

# Time: O(N)
# Space: O(1)