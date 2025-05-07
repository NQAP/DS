import argparse
import time


class MyNode(object):
    # Do Not Modify
    def __init__(self, value):
        self.value = value
        self.down = None

    def __repr__(self):
        return 'Node%s' % (self.value)


class MyStack(object):
    def __init__(self):
        self.num_element = 0
        # root is set on the right of the last element 
        self.root = MyNode(None)

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty stack')
            return
        else:
            self.num_element -= 1
            # ---TODO:
            # Record the last element value
            # Connect root >> the second last element
            # Return the last element value
            # ---
            node = self.root.down
            self.root.down = node.down
            node.down = None
            return node

    def push(self, node):
        self.num_element += 1
        # ---TODO:
        # Connect the last element >> inserted node
        # Connect the inserted node >> root
        # ---
        node.down = self.root.down
        self.root.down = node

    def __repr__(self):
        ret = ''
        node = self.root.down
        while node is not None:
            ret = '>>' + str(node) + ret
            node = node.down
        return ret

class MyQueue(object):
    def __init__(self):
        self.num_element = 0
        # root is set on the down of the first element 
        self.root = MyNode(None)
        # end is a pointer of the last element 
        self.end = self.root

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty queue')
            return
        else:
            self.num_element -= 1
            # ---TODO:
            # Record the first element value
            # Connect root >> the second element
            # if num_element == 0, connect end << root
            # Return the first element value
            # ---
            node = self.root.down
            self.root.down = node.down
            if self.root.down is None:
                self.end = self.root

    def push(self, node):
        self.num_element += 1
        # ---TODO:
        # Connect the last element >> inserted node
        # Connect the end << inserted node
        # ---
        if self.root.down is None:
            self.root.down = node
        self.end.down = node
        self.end = node

    def __repr__(self):
        ret = ''
        node = self.root.down
        while node is not None:
            ret = ret + '>>' + str(node)
            node = node.down
        return ret

class MyQueue_By_MyStack(object):
    def __init__(self):
        self.num_element = 0
        self.stack1 = MyStack()
        self.stack2 = MyStack()

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty queue')
            return
        else:
            self.num_element -= 1
            # ---TODO:
            # Pop the first element
            # ---
            if self.stack1.root.down is not None:
                self.stack1.pop()
            else:
                while self.stack2.root.down is not None:
                    node = self.stack2.pop()
                    self.stack1.push(node)
                self.stack1.pop()

    def push(self, node):
        self.num_element += 1
        # ---TODO:
        # Push the inserted node to the end of the queue
        # ---
        self.stack2.push(node)

    def __repr__(self):
        ret = 'Stack1: ' + str(self.stack1) + ', Stack2: ' + str(self.stack2)
        return ret

def main_stack(input_file, output_file1, has_ofile):
    myStack = MyStack()
    ifile = open(input_file)
    if has_ofile:
        ofile1 = open(output_file1, 'w')
    else:
        ofile1 = None
    for line in ifile.readlines():
        items = line.strip().split(" ")
        if items[0] == 'PUSH':
            myVal = int(items[1])
            myStack.push(MyNode(myVal))
        else:
            myStack.pop()
        if has_ofile:
            ofile1.write(str(myStack) + '\n')

def main_queue(input_file, output_file2, has_ofile):
    myQueue = MyQueue()
    ifile = open(input_file)
    if has_ofile:
        ofile2 = open(output_file2, 'w')
    else:
        ofile2 = None
    for line in ifile.readlines():
        items = line.strip().split(" ")
        if items[0] == 'PUSH':
            myVal = int(items[1])
            myQueue.push(MyNode(myVal))
        else:
            myQueue.pop()
        if has_ofile:
            ofile2.write(str(myQueue) + '\n')

def main_queue_by_stack(input_file, output_file3, has_ofile):
    myQueue_by_myStack = MyQueue_By_MyStack()
    ifile = open(input_file)
    if has_ofile:
        ofile3 = open(output_file3, 'w')
    else:
        ofile3 = None
    for line in ifile.readlines():
        items = line.strip().split(" ")
        if items[0] == 'PUSH':
            myVal = int(items[1])
            myQueue_by_myStack.push(MyNode(myVal))
        else:
            myQueue_by_myStack.pop()
        if has_ofile:
            ofile3.write(str(myQueue_by_myStack) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='./input_1.txt')
    parser.add_argument('--output1', default='')
    parser.add_argument('--output2', default='')
    parser.add_argument('--output3', default='')
    parser.add_argument('--test', default='')
    args = parser.parse_args()
    has_ofile1 = len(args.output1) > 0
    has_ofile2 = len(args.output2) > 0
    has_ofile3 = len(args.output3) > 0
    test = -1
    if(len(args.test) > 0):
        test = int(args.test)
    for i in range(3):
        ts = time.time()
        if i == 0:
            if test == 0 or test == -1:
                main_stack(args.input, args.output1, has_ofile1)
            te = time.time()
            if not has_ofile1:
                print('stack run time of %s: %.5fs' % (args.input, te - ts))
        elif i == 1:
            if test == 1 or test == -1:
                main_queue(args.input, args.output2, has_ofile2)
            te = time.time()
            if not has_ofile2:
                print('queue run time of %s: %.5fs' % (args.input, te - ts))
        else:
            if test == 2 or test == -1:
                main_queue_by_stack(args.input, args.output3, has_ofile3)
            te = time.time()
            if not has_ofile3:
                print('queue_by_stack run time of %s: %.5fs' % (args.input, te - ts))
