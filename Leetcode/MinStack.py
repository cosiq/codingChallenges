# Design a stack that supports push, pop, top, and 
# retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:
	def __init__(self):
		self.arr, self.min = [], []

	def push(self, x):
		if self.min: 
			if self.min[-1][0] == x: self.min[-1][1] += 1
			elif self.min[-1][0] > x: self.min.append([x, 1])
		else: self.min.append([x, 1])
		self.arr.append(x)

	def pop(self):
		if self.arr: 
			item = self.arr.pop()
			if item == self.min[-1][0]:
				self.min[-1][1] -= 1
				if self.min[-1][1] == 0: self.min.pop()
			return item
		return None

    def top(self): return self.arr[-1] if self.arr else None
    def getMin(self): return self.min[-1][0] if self.min else None




