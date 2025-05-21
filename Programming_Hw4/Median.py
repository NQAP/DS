##Important! You shouldn't use statistics library! ("import statistics" is not allowed)

import math
class MinHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
        
    def getSize(self):
        return self.size
    
    def insert(self, item): #insert new item
        
    ### TODO ### 
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        i = self.size
        while i > 0:
            if self.array[(i - 1) // 2] > self.array[i]:
                temp = self.array[(i - 1) // 2]
                self.array[(i - 1) // 2] = self.array[i]
                self.array[i] = temp
                i = (i - 1) // 2
            else:
                break
        self.size += 1

    def peek(self):  #Find Minimum item
        if self.size == 0:
            return
        else:
            return self.array[0]
        
    def removeMin(self):

    ### TODO ###
    ### You need not return or print anything with this function. ###
        self.size -= 1
        i = 0
        self.array[i] = self.array[self.size]
        self.array.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < self.size and self.array[left] < self.array[smallest]:
                smallest = left
            if right < self.size and self.array[right] < self.array[smallest]:
                smallest = right
            if smallest != i:
                temp = self.array[i]
                self.array[i] = self.array[smallest]
                self.array[smallest] = temp
                i = smallest
            else:
                break

    def showMinHeap(self):  #Show MinHeap with array
        return self.array

class MaxHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0

    def getSize(self):
        return self.size
    
    def insert(self, item): #insert new item

    ### TODO ###
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        i = self.size
        while i > 0:
            if self.array[(i - 1) // 2] < self.array[i]:
                temp = self.array[(i - 1) // 2]
                self.array[(i - 1) // 2] = self.array[i]
                self.array[i] = temp
                i = (i - 1) // 2
            else:
                break
        self.size += 1

    def peek(self):    #Find Maximum item
        if self.size == 0:
            return
        else:
            return self.array[0]
        
    def removeMax(self):   #Find Maximum item
    
    ### TODO ###
    ### You need not return or print anything with this function. ###
        self.size -= 1
        i = 0
        self.array[i] = self.array[self.size]
        self.array.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < self.size and self.array[left] > self.array[largest]:
                largest = left
            if right < self.size and self.array[right] > self.array[largest]:
                largest = right
            if largest != i:
                temp = self.array[i]
                self.array[i] = self.array[largest]
                self.array[largest] = temp
                i = largest
            else:
                break

    def showMaxHeap(self):   #Show MaxHeap with array
        return self.array

class FindMedian: 
    def __init__(self):
    
    ### TODO ###
    ### Your own data structure. Implementing with heap structure is highly recommended. ###
        self.rightmin = MinHeap()
        self.leftmax = MaxHeap()

    def AddNewValues(self, NewValues):  # Add NewValues(a list of items) into your data structure
    
    ### TODO ### 
    ### input: a list of values ###
    ### You need not return or print anything with this function. ###

        # We hope that minheap size = maxheap size + 1 or maxheap size

        for value in NewValues:

            # Insert value
            if self.leftmax.size == 0:
                self.leftmax.insert(value)
            elif value > self.leftmax.peek():
                self.rightmin.insert(value)
            else:
                self.leftmax.insert(value)

            # Balanced heap size
            if self.rightmin.size > self.leftmax.size + 1:
                temp = self.rightmin.peek()
                self.leftmax.insert(temp)
                self.rightmin.removeMin()
            elif self.rightmin.size < self.leftmax.size:
                temp = self.leftmax.peek()
                self.rightmin.insert(temp)
                self.leftmax.removeMax()


    def ShowMedian(self):  # Show Median of your data structure
    
    ### TODO ### 
    ### You need not print anything but "return Median". ###
    ###The return value should always be a float number. ###
        size = self.rightmin.size + self.leftmax.size
        if size % 2 == 0:
            median = (self.leftmax.peek() + self.rightmin.peek()) / 2.0
        else:
            median = float(self.rightmin.peek())
        return median

    def RemoveMedian(self): # Remove median
    
    ### TODO ###
    ### You need not return or print anything with this function. ###
    ### If there are even number of elements, remove the larger one ###
    ### For example, if array=[1, 2, 3, 5], remove 3 ###

        
        self.rightmin.removeMin()
        if self.rightmin.size < self.leftmax.size:
            temp = self.leftmax.peek()
            self.rightmin.insert(temp)
            self.leftmax.removeMax()