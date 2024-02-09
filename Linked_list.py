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

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_begining(data)
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.get_length() == 0:
            self.insert_at_begining(data_to_insert)
            return
        # Search for first occurance of data_after value in linked list
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                # Now insert data_to_insert after data_after node
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next  # we are pointing the single node to None
            return
        # Remove first node that contains data
        try:
            itr = self.head
            while itr:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break
                itr = itr.next
        except AttributeError:
            print('Element not found in the linkedlist.')

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


# if __name__ == '__main__':
#     ll = LinkedList()
#     # ll.insert_at_begining(5)
#     # ll.insert_at_begining(89)
#     # ll.insert_at_end(19)
#     ll.insert_values(['Apple', 'Banana', 'Carrot', 'Dry fruits'])
#     length = ll.get_length()
#     print(length)
#     ll.insert_after_value('Banana', 'Mango')
#     ll.insert_at(3, "Dates")
#     # ll.remove_at(-2)
#     # ll.remove_by_value('Banana')
#     ll.print()
