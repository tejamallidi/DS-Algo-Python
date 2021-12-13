class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # if data already exists in the tree return
        if data == self.data:
            return

        if data < self.data:
            # add data to left subtree if it exists, else create it with the given data
            if self.left:
                # if self.left have a value, add this node as a child to it
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            # add data to right subtree if it exists, else create it with the given data
            if self.right:
                # if self.right have a value, add this node as a child to it
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def pre_order_traversal(self):
        elements = []

        # visit base node
        # or when initiating the list make it as - elements = [self.data]
        elements.append(self.data)

        # visit left node, append elements to list
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right node, append elements to list
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def in_order_traversal(self):
        elements = []

        # visit left tree, append to elements list
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree, append to elements list
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # visit left tree, append to elements list
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right tree, append to elements list
        if self.right:
            elements += self.right.post_order_traversal()

        # visit base node
        elements.append(self.data)

        return elements

    def search(self, val):
        # if root node is the val
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        sum = 0
        if self.data:
            sum = self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum

    def delete(self, val):
        if val < self.data:
            # check if left subtree exists
            if self.left:
                # recursively call delete function on left sub tree
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # leaf node - unable to find the val in the tree
            if self.left is None and self.right is None:
                return None
            if self.left is None:  # we have right but not left
                return self.right
            if self.right is None:  # we have left but not right
                return self.left
            # # find_min in the right subtree of the current node
            # min_val = self.right.find_min()
            # # copy minimum value to the current position
            # self.data = min_val
            # # delete the duplicate from right subtree
            # self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.left = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(14))
    # print("Min:", numbers_tree.find_min())
    # print("Max:", numbers_tree.find_max())
    # print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal before deleting 23:",
          numbers_tree.in_order_traversal())
    # print("Pre order traversal:", numbers_tree.pre_order_traversal())
    # print("Post order traversal:", numbers_tree.post_order_traversal())
    numbers_tree.delete(17)
    print("In order traversal after deleting 23:",
          numbers_tree.in_order_traversal())
    # countries = ['India', 'USA', 'Germany', 'China', 'Sri Lanka', 'Pakistan']
    # country_tree = build_tree(countries)
    # print(country_tree.in_order_traversal())
    # print(country_tree.search('USA'))
    # print(country_tree.search('UK'))
