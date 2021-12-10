class TreeNode:
    def __init__(self, data):
        # for assignment instead of data we can declare name, designation as class variables
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        # whenever we are adding a child, we will be adding to the self object as it will be the parent of the child node
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        # p be parent of the current node
        p = self.parent
        while p:  # traverse through parent nodes of current and increment level
            level += 1
            p = p.parent
        return level

    # def print_tree(self):
    #     spaces = ' ' * self.get_level() * 3
    #     prefix = spaces + '|__' if self.parent else ""
    #     print(prefix + self.data)
    #     # traverse through children recursively
    #     if self.children:
    #         for child in self.children:
    #             child.print_tree()

    # For assignment
    def print_tree(self, param):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        if param == 'name':
            print(prefix + str(self.data['name']))
        elif param == 'designation':
            print(prefix + str(self.data['designation']))
        elif param == 'both':
            print(prefix + str(self.data['name']) +
                  ' ('+str(self.data['designation'])+')')
        # traverse through children recursively
        # if self.get_level() <= level: # this is the code to be added for assignment to print the tree till that level
        if self.children:
            for child in self.children:
                child.print_tree(param)


def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    cellphone = TreeNode('Cell Phone')
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('Samsung'))
    cellphone.add_child(TreeNode('Pixel'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Sony'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


def build_management_tree():
    root = TreeNode({'name': 'Nilupul', 'designation': 'CEO'})

    cto = TreeNode({'name': 'Chinmayi', 'designation': 'CTO'})
    infra_head = TreeNode(
        {'name': 'Vishwa', 'designation': 'Infrastructure Head'})
    cto.add_child(infra_head)
    cto.add_child(
        TreeNode({'name': 'Aamir', 'designation': 'Application Head'}))

    infra_head.add_child(
        TreeNode({'name': 'Dhaval', 'designation': 'Cloud Manager'}))
    infra_head.add_child(
        TreeNode({'name': 'Abhijit', 'designation': 'App Manager'}))

    hr_head = TreeNode({'name': 'Gels', 'designation': 'HR Head'})
    hr_head.add_child(
        TreeNode({'name': 'Peter', 'designation': 'Recruitment Manager'}))
    hr_head.add_child(
        TreeNode({'name': 'Waqas', 'designation': 'Policy Manager'}))

    root.add_child(cto)
    root.add_child(hr_head)
    return root


if __name__ == '__main__':
    # root = build_product_tree()
    # root.print_tree()
    root_node = build_management_tree()
    print('***** Employees Names *****')
    root_node.print_tree("name")
    print('***** Designation Hierarchy *****')
    root_node.print_tree("designation")
    print('***** Employees & Designations *****')
    root_node.print_tree("both")


'''
Below is the management hierarchy of a company.

Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. As shown below,

Here is how your main function should will look like,

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
'''
