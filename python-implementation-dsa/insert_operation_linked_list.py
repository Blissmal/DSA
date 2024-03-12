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

    def insert(self, data, index):
        """
        Insert a new node containin data at index position
        Insertion takes O(1) time but finding the node at the
        insertion point takes O(n) time

        Takes overall O(n) time
        """
        
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

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
n = l.insert(45, 4)
print(n)
print(l)
