class Node:
    """
    An object for storing a single node of a linked list,
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Adds new node containing data at the head of a list
        This operation takes constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the node or none if the key is doesnt exist
        Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
                
        return current

    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)



l = LinkedList()
l.add(10)
l.add(20)
l.add(45)
l.add(15)
n = l.remove(45, 4)
print(n)
print(l)
