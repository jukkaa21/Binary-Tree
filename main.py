class Node:
    def __init__(self, key_, value_, left_=None, right_=None):
        self.key = key_
        self.value = value_
        self.left = left_
        self.right = right_


class BinaryTree:
    def __init__(self):
        self.root = None

    def search_rec(self, key, curr_node):
        if key == curr_node.key:
            return curr_node.value
        elif key < curr_node.key:
            curr_node = curr_node.left
        elif key > curr_node.key:
            curr_node = curr_node.right

        if curr_node is None:
            return None
        else:
            return self.search_rec(key, curr_node)

    def search(self, key):
        curr_node = self.root
        return self.search_rec(key, curr_node)

    def insert_rec(self, key, data, parent_node):
        if key == parent_node.key:
            parent_node.value = data
            return
        if key < parent_node.key and parent_node.left is not None:
            self.insert_rec(key, data, parent_node.left)
            return
        if key > parent_node.key and parent_node.right is not None:
            self.insert_rec(key, data, parent_node.right)
            return
        if key < parent_node.key and parent_node.left is None:
            parent_node.left = Node(key, data)
            return
        if key > parent_node.key and parent_node.right is None:
            parent_node.right = Node(key, data)
            return

    def insert(self, key, data):
        if self.root is None:
            self.root = Node(key, data)
            return
        else:
            return self.insert_rec(key, data, self.root)

    def delete(self, key):
        curr_node = self.root
        parent_right = None
        parent_left = None
        while key != curr_node.key:
            if key < curr_node.key:
                parent_left = curr_node
                parent_right = None
                curr_node = curr_node.left
            elif key > curr_node.key:
                parent_left = curr_node
                parent_right = None
                curr_node = curr_node.right

            if curr_node is None:
                return None

        node_to_delete = curr_node

        if node_to_delete.right is None and node_to_delete.left is None:
            if parent_right is not None:
                parent_right.right = None
            elif parent_left is not None:
                parent_left.left = None

        elif node_to_delete.right is None and node_to_delete.left is not None:
            node_to_delete.key = node_to_delete.left.key
            node_to_delete.value = node_to_delete.left.value
            node_to_delete.left = node_to_delete.left.left
        elif node_to_delete.right is not None and node_to_delete.left is None:
            node_to_delete.key = node_to_delete.right.key
            node_to_delete.value = node_to_delete.right.value
            node_to_delete.left = node_to_delete.right.left
        elif node_to_delete.right is not None and node_to_delete.left is not None:

            smallest_from_right = node_to_delete.right
            smallests_parent = node_to_delete

            i = 0
            while smallest_from_right.left is not None:
                smallests_parent = smallest_from_right
                smallest_from_right = smallest_from_right.left
                i+=1

            node_to_delete.key = smallest_from_right.key
            node_to_delete.value = smallest_from_right.value

            if i > 0:
                smallests_parent.left = smallest_from_right.right
            if i == 0:
                node_to_delete.right = smallest_from_right.right

    def height_rec(self, node):
        if node is None:
            return 0
        left_height = self.height_rec(node.left)
        right_height = self.height_rec(node.right)
        if left_height >= right_height:
            return left_height + 1
        else:
            return right_height + 1

    def height(self):
        curr_node = self.root
        return self.height_rec(curr_node)

    def str_rec(self, node):
        wynik = ""
        if node is not None:
            wynik += self.str_rec(node.left)

            wynik += f"{node.key} {node.value},"

            wynik += self.str_rec(node.right)

        return wynik

    def __str__(self):
        wynik = "[" + self.str_rec(self.root)
        wynik = wynik[:-1] + "]"
        return wynik

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self.__print_tree(node.left, lvl + 5)



dict = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}

tree = BinaryTree()

for key in dict:
    tree.insert(key, dict[key])

# print 2D tree
tree.print_tree()

# print tree as a list
print(tree)

print(tree.search(24))

tree.insert(20, 'AA')
tree.insert(6, 'M')
tree.delete(62)
tree.insert(59, 'N')
tree.insert(100, 'P')
tree.delete(8)
tree.delete(15)
tree.insert(55, 'R')
tree.delete(50)
tree.delete(5)
tree.delete(24)

# tree as a list
print(tree)

# 2D tree
tree.print_tree()
