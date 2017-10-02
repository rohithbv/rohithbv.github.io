from linked_lists_class import ListNode
from linked_lists_class import LinkedList

def addLinkedLists(l1, l2):
	''' Adds elements in the linked lists and returns a new list with the sums '''
	l1Runner = l1.head
	l2Runner = l2.head
	result = LinkedList()
	sum = carry = 0
	while l1Runner or l2Runner:
		l1Val = 0 if l1Runner == None else l1Runner.getData()
		l2Val = 0 if l2Runner == None else l2Runner.getData()
		sum = l1Val + l2Val + carry
		carry = 0 if sum < 10 else 1
		result.addNode(sum%10)
		l1Runner = None if l1Runner == None else l1Runner.next
		l2Runner = None if l2Runner == None else l2Runner.next
	if carry == 1:
		result.addNode(carry)
	return result

def weaveLinkedLists(l1, l2):
	''' Weaves elements of linked lists and returns list '''
	l1Runner = l1.head
	l2Runner = l2.head
	while l1Runner or l2Runner:
		l1Next = None if l1Runner == None else l1Runner.next
		l2Next = None if l2Runner == None else l2Runner.next
		if l1Runner != None and l2Runner != None: l1Runner.next = l2Runner
		if l2Runner != None and l1Next != None: l2Runner.next = l1Next
		if l2Runner != None: l2Runner = l2Next
		if l1Runner != None: l1Runner = l1Next
	if l1.head: return l1
	else: return l2


def linkedList_test1():
	''' Basic linked list test - create & add nodes'''
	myLL = LinkedList()
	myLL.addNode(1)
	myLL.addNode(2)
	myLL.addNode(0)
	result = myLL.parseList()
	print "Linked list values = %s" % result

def linkedList_test2():
	''' Adds the nodes in the two linked lists and returns a new list '''
	l1 = LinkedList()
	l2 = LinkedList()
	for i in range(5, 7):
		l1.addNode(i)
	for i in range(5, 8):
		l2.addNode(i)
	print "List-1 = %s" % l1.parseList()
	print "List-2 = %s" % l2.parseList()
	result = addLinkedLists(l1, l2)
	print "result list = %s" % result.parseList()

def linkedList_test3():
	''' Weaves each element of a linked list and returns a valid list '''
	l1 = LinkedList()
	l2 = LinkedList()
	for i in range(1, 4):
		l1.addNode(i)
	for i in range(4, 8):
		l2.addNode(i)
	print "List-1 = %s" % l1.parseList()
	print "List-2 = %s" % l2.parseList()
	print "result list = %s" % weaveLinkedLists(l1, l2).parseList()

def linkedList_test4():
	''' Reverses a linked list permanently '''
	myLL = LinkedList()
	for i in range(5):
		myLL.addNode(i)
	result = myLL.parseList()
	print "Linked list values = %s" % result
	myLL.reverseLinkedList()
	result = myLL.parseList()
	print "Linked list values = %s" % result
	myLL.reverseLinkedList()
	result = myLL.parseList()
	print "Linked list values = %s" % result

def linkedList_test5():
	''' Copies a linked list and returns a new list '''
	myLL = LinkedList()
	for i in range(6):
		myLL.addNode(i)
	result = myLL.parseList()
	print "Linked list values = %s" % result
	newLL = myLL.copyLinkedList()
	result = myLL.parseList()
	print "Linked list values = %s" % result

def begin():
	linkedList_test5()

if __name__ == '__main__':
	begin()
