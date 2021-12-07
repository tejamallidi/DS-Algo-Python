class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        # create a node with data, next pointing to head.next
        node = Node(data, self.head)
        # assign head to this node to insert at begining
        self.head = node

    def insert_at_end(self, data):
        # check if the linked list is empty, if yes insert at begining
        if self.head is None:
            self.head = Node(data, None)
            return
        # if not traverse through last element and insert at that position
        itr = self.head
        while itr.next:  # if itr.next has some value I am not at last element
            itr = itr.next
        # out of loop mean I am at last position, add your node here
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        # insert the elements of data_list by removing existing elements in linked list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        # iterate through linked list
        itr = self.head
        llstr = ''
        while itr:  # there is a item in the traversal
            # append the data to llstr to print at the end
            llstr += str(itr.data) + '-->'
            itr = itr.next  # move to next element
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(89)
    # ll.insert_at_end(19)
    ll.insert_values(['Apple', 'Banana', 'Carrot', 'Dry fruits'])
    length = ll.get_length()
    print(length)
    ll.remove_at(-2)
    ll.print()
