class ListNode:
	def __init__(self, data):
		self.data = data
		self.next = None
	def getData(self):
		return self.data
	def setData(self, data):
		self.data = data
	def getNext(self):
		return self.next
	def setNext(self, next):
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
		self.totalNodes = 0
	def getTailNode(self):
		runner = self.head
		while runner.next:
			runner = runner.next
		return runner
	def addNode(self, data):
		if not self.head:
			self.head = ListNode(data)
		else:
			tail = self.getTailNode()
			tail.next = ListNode(data)
		self.totalNodes += 1
	def parseList(self):
		elem = self.head
		result = list()
		while elem:
			result.append(elem.getData())
			elem = elem.next
		return result
	def reverseLinkedList(self):
		''' Reverses the linked list '''
		if self.head:
			oldNode = newNode = None
			node = self.head
			while node:
				newNode = node.next
				node.next = oldNode
				oldNode = node
				node = newNode
			self.head = oldNode
	def copyLinkedList(self):
		''' Copies this linked list and returns a new list'''
		if self.head:
			result = LinkedList()
			node = self.head
			while node:
				result.addNode(node.data)
				node = node.next
			return result
