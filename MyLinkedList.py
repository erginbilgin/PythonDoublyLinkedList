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
    def insertItem(self, value, position):
        node = Node(value)
        if self.count > position:
            if position == 0:
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                currentNode = self.head
                for i in range(0, position):
                    currentNode = currentNode.next
                node.next = currentNode
                node.prev = currentNode.prev
                currentNode.prev.next = node
                currentNode.prev = node
            self.count += 1
    def removeItem(self, position):
        if self.count > position:
            if self.count != 1:
                if position == 0:
                    self.head.next.prev = head.prev
                    self.head = head.next
                if position == self.count-1:
                    self.tail.prev.next = tail.next
                    self.tail = tail.prev
                if position > 0 and position < self.count-1:
                    currentNode = self.head
                    for i in range(0, position):
                        currentNode = currentNode.next
                    currentNode.next.prev = currentNode.prev
                    currentNode.prev.next = currentNode.next
            else:
                    head = Node()
                    tail = Node()
            self.count -= 1
    def replaceItem(self, itemToReplace, position):
        if self.count > position:
            currentNode = self.head
            if position == 0:
                currentNode.value = itemToReplace
            else:
                for i in range(0, position):
                    currentNode = currentNode.next
                currentNode.value = itemToReplace
    def getItemAt(self, position):
        if self.count > position:
            currentNode = self.head
            if position == 0:
                return currentNode.value
            else:
                for i in range(0, position):
                    currentNode = currentNode.next
                return currentNode.value
        else:
            return None
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
    def printInverse(self):
        output = '['
        currentNode = self.tail
        while currentNode is not None:
            output += str(currentNode.value)
            currentNode = currentNode.prev
            if currentNode is not None:
                output += ', '
        output += ']'
        print(output)
