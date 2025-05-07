import argparse


class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self.value)


class BS_tree():
    def __init__(self):
        self.root = None
        self.treelist = []

    def inorder(self, output):      # print the in-order traversal of binary search tree
        # TODO
        curr = self.root
        temp_stack = []
        ans = []
        while curr is not None or len(temp_stack) > 0:
            while curr is not None:
                temp_stack.append(curr)
                curr = curr.left_child
            curr = temp_stack.pop()
            ans.append(curr.value)
            curr = curr.right_child
        output_line = [str(a) for a in ans]
        for element in output_line:
            output.write(element + ' ')
        output.write('\n')

    def preorder(self, output):     # print the pre-order traversal of binary search tree
        # TODO
        curr = self.root
        temp_stack = []
        ans = []
        while curr is not None or len(temp_stack) > 0:
            while curr is not None:
                ans.append(curr.value)
                temp_stack.append(curr)
                curr = curr.left_child
            curr = temp_stack.pop()
            curr = curr.right_child
        output_line = [str(a) for a in ans]
        for element in output_line:
            output.write(element + ' ')
        output.write('\n')

    def postorder(self, output):    # print the post-order traversal of binary search tree
        # TODO
        curr = self.root
        temp_stack = []
        temp_stack2 = []
        ans = []
        if curr is not None:
            temp_stack.append(curr)
        while len(temp_stack) > 0:
            curr = temp_stack.pop()
            temp_stack2.append(curr)
            if curr.left_child is not None:
                temp_stack.append(curr.left_child)
            if curr.right_child is not None:
                temp_stack.append(curr.right_child)
        while len(temp_stack2) > 0:
            curr = temp_stack2.pop()
            ans.append(curr.value)
        output_line = [str(a) for a in ans]
        for element in output_line:
            output.write(element + ' ')
        output.write('\n')

    def find_max(self, output):     # print the maximum number in binary search tree
        # TODO
        curr = self.root
        if curr is None:
            return
        while curr.right_child is not None:
            curr = curr.right_child
        print(curr.value)
        output.write(str(curr.value) + '\n')

    def find_min(self, output):     # print the minimum number in binary search tree
        # TODO
        curr = self.root
        if curr is None:
            return
        while curr.left_child is not None:
            curr = curr.left_child
        print(curr.value)
        output.write(str(curr.value) + '\n')

    def insert(self, key):          # insert one node
        if self.root:
            self._insert(key, self.root)
        else:
            self.root = Node(key)

    def delete(self, key):          # delete one node
        # TODO
        curr = self.root
        parent = None
        succ = None
        while curr is not None:
            if key < curr.value:
                parent = curr
                curr = curr.left_child
            elif key > curr.value:
                parent = curr
                curr = curr.right_child
            else:
                break
        if curr is None:
            return
        if parent is None:
            if curr.left_child is None and curr.right_child is None:
                self.root = None
            elif curr.left_child is None:
                self.root = curr.right_child
            elif curr.right_child is None:
                self.root = curr.left_child
            else:
                parent = curr
                succ = curr.right_child
                while succ.left_child is not None:
                    parent = succ
                    succ = succ.left_child
                curr.value = succ.value
                parent.left_child = None
            return
        if curr.left_child is None and curr.right_child is None:
            if parent.value < curr.value:
                parent.right_child = None
            else:
                parent.left_child = None
        elif curr.left_child is None:
            if parent.value < curr.value:
                parent.right_child = curr.right_child
            else:
                parent.left_child = curr.right_child
        elif curr.right_child is None:
            if parent.value < curr.value:
                parent.right_child = curr.left_child
            else:
                parent.left_child = curr.left_child
        else:
            parent = curr
            succ = curr.right_child
            while succ.left_child is not None:
                parent = succ
                succ = succ.left_child
            curr.value = succ.value
            parent.left_child = None

    def level(self, output):        # print the height of binary search tree(leaf = 0)
        # TODO
        curr = self.root
        temp_stack = []
        tree_height = 0
        tree_height_list = []
        while curr is not None or len(temp_stack) > 0:
            while curr is not None:
                tree_height += 1
                temp_stack.append(curr)
                curr = curr.left_child
            curr = temp_stack.pop()
            tree_height_list.append(tree_height)
            tree_height -= 1
            curr = curr.right_child
        h = max(tree_height_list, default=0)
        output.write(str(h) + '\n')
    # print the internal node in binary search tree from the smallest to the largest
    def internalnode(self, output):
        # TODO
        curr = self.root
        temp_stack = []
        ans = []
        while curr is not None or len(temp_stack) > 0:
            while curr is not None:
                temp_stack.append(curr)
                curr = curr.left_child
            curr = temp_stack.pop()
            if curr.left_child is not None or curr.right_child is not None:
                ans.append(curr.value)
            curr = curr.right_child
        output_line = [str(a) for a in ans]
        for element in output_line:
            output.write(element + ' ')
        output.write('\n')

    def leafnode(self, output):     # print the leafnode in BST from left to right
        # TODO
        curr = self.root
        temp_stack = []
        ans = []
        while curr is not None or len(temp_stack) > 0:
            while curr is not None:
                temp_stack.append(curr)
                curr = curr.left_child
            curr = temp_stack.pop()
            if curr.left_child is None and curr.right_child is None:
                ans.append(curr.value)
            curr = curr.right_child
        output_line = [str(a) for a in ans]
        for element in output_line:
            output.write(element + ' ')
        output.write('\n')

    def _insert(self, key, curNode):  # recursively insert node
        if key < curNode.value:
            if curNode.left_child:
                self._insert(key, curNode.left_child)
            else:
                curNode.left_child = Node(key)
        elif key > curNode.value:
            if curNode.right_child:
                self._insert(key, curNode.right_child)
            else:
                curNode.right_child = Node(key)
        else:
            print("No way!!! There is the same value in this tree.")

    def showtree(self, curNode):
        self.treelist.append(curNode.value)

    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        #########################
        output = open(output_path, 'w')
        with open(input_path, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()


if __name__ == '__main__':
    #########################
    # DO NOT MODIFY CODES HERE
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str,
                        default='./input_3.txt', help="Input file root.")
    parser.add_argument("--output", type=str,
                        default='./output_3.txt', help="Output file root.")
    args = parser.parse_args()

    BS = BS_tree()
    BS.main(args.input, args.output)
