from Node import Node

class MyLinkedList(object):
	count = 0
	head = None
	tail = None
	#def __init__(self):
	def isEmpty(self):
		return self.count == 0
	def addItem(self, value):
		node = Node(value)
		if self.isEmpty():
			self.head = node
			self.tail = node
		else:
			node.prev = self.tail
			self.tail.next = node
			self.tail = node
		self.count += 1
	def printList(self):
		output = '['
		currentNode = self.head
		while currentNode is not None:
			output += str(currentNode.value)
			currentNode = currentNode.next
			if currentNode is not None:
				output += ', '
		output += ']'
		print(output)