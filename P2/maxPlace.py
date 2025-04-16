import numpy as np

class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = self
        
    def __repr__(self):
        return 'Node%s' % (self.value)

class Stack(object):
    def __init__(self):
        self.size = 0
        self.root = Node(None)
    
    def push(self,node):
        self.size += 1

        node.prev = self.root.prev
        self.root.prev = node
    
    def pop(self):
        if self.size<1:
            raise ValueError('Can not execute pop() on an empty stack')
        else:
            self.size -= 1

            ret_node = self.root.prev
            if self.size == 0:
                self.root.prev = self
            else:
                self.root.prev = self.root.prev.prev

            return ret_node.value
    
    def peak(self):
        if self.size<1:
            raise ValueError('Can not execute peak() on an empty stack')
        return self.root.prev.value
        
    def __repr__(self):
        ret = ''
        node = self.root.prev
        for i in range(self.size):
            ret = ret + '>>' + str(node)
            node = node.prev
        return ret

def Ver_1D_increase(map_array:list[int])-> int:
    # input: map_array
    # map_array is a list consisting of increasing number.
    # Representing land heights from left to right.
    max_area = 0
    # TODO: return the max area
    n = len(map_array)
    for i in map_array:
        max_area = max(max_area, i * n)
        n = n - 1
    return max_area 

def Ver_1D_general(map_array:list[int])-> int:
    # input: map_array is a 1-dimensional array consisting of non negative integer. each number means how much empty place above its.
    # Goal: return the max rectangle area with time complexity O(n), n is the length of map_array
    # Hint: Can think of it as a lot of Ver_1D_increase cases
    max_area = 0 
    # TODO: return max rectangle area
    stack_value = Stack() #You may decide whether to use the stack or not.
    stack_index = Stack()
    n = len(map_array)
    for i in range(n):
        val_node = Node(None)
        val_node.value = map_array[i]
        val_node.prev = None
        idx_node = Node(None)
        idx_node.value = i
        idx_node.prev = None
        if stack_value.size < 1:
            if map_array[i] == 0:
                continue
            stack_value.push(val_node)
            stack_index.push(idx_node)
        elif map_array[i] > stack_value.peak():
            stack_value.push(val_node)
            stack_index.push(idx_node)
        elif map_array[i] < stack_value.peak():
            while map_array[i] < stack_value.peak():
                val = stack_value.pop()
                idx = stack_index.pop()
                max_area = max(max_area, val * (i - idx))
                idx_node.value = idx
                if stack_value.size < 1:
                    break
            if stack_value.size < 1:
                if map_array[i] == 0:
                    continue
                stack_value.push(val_node)
                stack_index.push(idx_node)
            elif map_array[i] > stack_value.peak():
                stack_value.push(val_node)
                stack_index.push(idx_node)
    
    while stack_value.size > 0:
        val = stack_value.pop()
        idx = stack_index.pop()
        max_area = max(max_area, val * (n - idx))

    return max_area 



def Ver_2D(city_map:list[list[int]])-> int:
    # input: city_map is a 2-dimensional array consisting of 0 or 1. 0 means there is non-empty and 1 means empty place.
    # Goal: return the max rectangle area
    # Hint: can simplify each column as Ver_1D_general case.
    max_area = 0
    # TODO: return max rectangle area
    n = len(city_map[0])
    Gen_1D = [0] * n
    for city_list in city_map:
        for i in range(len(city_list)):
            if city_list[i] == 0:
                Gen_1D[i] = 0
            else:
                Gen_1D[i] = Gen_1D[i] + 1
        max_area = max(max_area, Ver_1D_general(Gen_1D))
    return max_area
