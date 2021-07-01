"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""
class my_first_class:
    def __init__(self,first):
        self.first = first

    
    def getstring(self):
        self.first = input("Enter a phrase : ")

    def printstring(self):
        print("UPPER : ",self.first.upper())

a = my_first_class(1)
a.getstring()
a.printstring()