"""
Author: Scott Choi, schoi@uoregon.edu
File Description: Contains Implementations for Stack and Queue, used to create a function, isPalindrome, that checks whether a given input is a Palindrome.
"""

class Node(object):
    """
    A class to represent a node.
    """
    def __init__(self, data = None, next_node = None):
        self.__data = data
        self.__next_node = next_node
            
    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data
    
    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    '''
    A class to represent Queue data structure 
    '''
    def __init__(self):
        self.__head = None
        self.__tail = None
    
    def enqueue(self, newData):
        '''
        Create a new node whose data is newData and whose next node is null
        Update head and tail.
        '''
        newNode = Node()
        newNode.setData(newData)
        #newNode.setNext(None) #redundant
        if self.isEmpty() == True:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.setNext(newNode)
            self.__tail = newNode

    def dequeue(self):
        '''Return the head of the Queue'''
        if self.isEmpty() == True:
            return None
        else:
            holdNode = self.__head
            self.__head = self.__head.getNext()
            return holdNode.getData()
    
    def isEmpty(self):
        '''Check if the Queue is empty.'''
        if self.__head == None:
            return True
        else:
            return False #redundant since I can just use isEmpty() != True
    
    def printQueue(self):
        '''Loop through your queue and print each Node's data.'''
        printList = []
        currNode = self.__head
        while currNode != None:
            printList.append(currNode.getData())
            currNode = currNode.getNext()
        return printList
         
class Stack(object):
    def __init__(self):
        ''' We want to initialize our Stack to be empty.'''
        self.__top = None
    
    def push(self, newData):
        '''
        We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top
        '''
        newNode = Node()
        newNode.setData(newData)
        newNode.setNext(self.__top)
        self.__top = newNode
    
    def pop(self):
        ''' 
        Return the Node that currently represents the top of the stack.
        Update top
        '''
        if self.isEmpty():
            return None
        else:
            holdNode = self.__top
            self.__top = self.__top.getNext()
            return holdNode.getData()
        
    def isEmpty(self):
        '''Check if the Stack is empty.'''
        if self.__top == None:
            return True
        else:
            return False
        
    def printStack(self):
        '''Loop through your stack and print each Node's data.'''
        printList = []
        currNode = self.__top
        while currNode != None:
            printList.append(currNode.getData())
            currNode = currNode.getNext()
        return printList
        
def isPalindrome(s):
    '''Uses the Queue and Stack class to test wheather a input, string, is a palindrome and returns a Boolean.'''
    myStack = Stack() 
    myQueue = Queue()
    for char in s:
        if char != ' ':
            myStack.push(char.lower())
    for char in s:
        if char != ' ':
            myQueue.enqueue(char.lower())
    if myStack.pop() != myQueue.dequeue():
        return False
    return True