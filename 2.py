"""""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def factorial(num):
    result = 1
    for i in range(2,num+1):
        result = i*result
    return result

"""
def fact(num):
    if(num==1):
        return 1
    else:
        result = num*fact(num)
"""

a = input("Enter numbers : ").split()
print("Factorial of given numbers : ",end='')
for i in range(0,len(a)):
    if(i==0):
        print(factorial(int(a[i])),end='')
    else:
        print(', ',factorial(int(a[i])),end='')