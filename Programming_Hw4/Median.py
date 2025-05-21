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

    def peek(self):  #Find Minimum item
        if self.size == 0:
            return
        else:
            return self.array[0]
        
    def removeMin(self):

    ### TODO ###
    ### You need not return or print anything with this function. ###

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

    def peek(self):    #Find Maximum item
        if self.size == 0:
            return
        else:
            return self.array[0]
        
    def removeMax(self):   #Find Maximum item
    
    ### TODO ###
    ### You need not return or print anything with this function. ###

    def showMaxHeap(self):   #Show MaxHeap with array
        return self.array

class FindMedian: 
    def __init__(self):

    ### TODO ###
    ### Your own data structure. Implementing with heap structure is highly recommended. ###

    def AddNewValues(self, NewValues):  # Add NewValues(a list of items) into your data structure
    
    ### TODO ### 
    ### input: a list of values ###
    ### You need not return or print anything with this function. ###

    def ShowMedian(self):  # Show Median of your data structure
    
    ### TODO ### 
    ### You need not print anything but "return Median". ###
    ###The return value should always be a float number. ###

    def RemoveMedian(self): # Remove median
    
    ### TODO ###
    ### You need not return or print anything with this function. ###
    ### If there are even number of elements, remove the larger one ###
    ### For example, if array=[1, 2, 3, 5], remove 3 ###