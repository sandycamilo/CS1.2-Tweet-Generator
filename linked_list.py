class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        count = 0 
        node = self.head
        while node is not None:
            node = node.next
            count += 1   
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        if self.is_empty():
            node = Node(item)
            self.head = node 
            self.tail = node 
        else: 
            node = Node(item)
            self.tail.next = node
            self.tail = self.tail.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        if self.is_empty():
            node = Node(item)
            self.head = node
            self.tail = node 
        else:
            node = Node(item)
            node.next = self.head 
            self.head = node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            result = quality(node.data) #helper function that checks data 
            if result:
                return node.data
            else: 
                node = node.next
        return None 

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        # empty list
        if self.is_empty(): 
            raise ValueError('Item not found')

        # assign iterators
        prev_node = self.head
        curr_node = self.head.next

        # head is item to delete
        if prev_node.data == item:
            if self.head == self.tail: #if you are deleting the only thing in the list
                self.tail = None 
            self.head = curr_node
            prev_node = None  # prev_node.next
            return

        # looping through the entire list
        while curr_node != None:
            print(curr_node)
            print(prev_node)
        #if we found the item that we are looking for 
            if curr_node.data == item:
                prev_node.next = curr_node.next
                curr_node = None
                #if we are deleting the tail node 
                if prev_node.next is None:
                    self.tail = prev_node
                return
            else:
                prev_node = curr_node 
                curr_node = curr_node.next


            #check if item is in head and tail (one item in list)
            # if item == prev_node.data or item == curr_node.next.data:
            #     prev_node = None 
            #     curr_node.next= None
            #     #check if item in head
            #     if item == prev_node.data:
            #         # prev_node = prev_node.next
            #         self.head = curr_node 
            #     #check if item in tail
            #     elif item == curr_node.next.data:     
            #         # curr_node.next = prev_node
            #         prev_node.next = None
            #     #middle case 
            #     elif item == curr_node.data:
            #         prev_node.next = curr_node.next
            #         return
        raise ValueError('Item not found')   
        
        #  # cur_node = self.head 
        # prev_node = None
        # while cur_node.data != item:
        #     prev_node = cur_node
        #     cur_node = cur_node.next  
        # cur_node = None 
        # def print_ll(self):
        #     current = self.head
        #     while current != None:
        #         print(current.data)
        #         current = current.next

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
    # ll = LinkedList(["a", "b", "c"])
    # ll.print_ll()
    # ll.delete("b")
    