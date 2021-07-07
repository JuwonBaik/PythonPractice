"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as 
its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
var = input("Enter 4 digit binary numbers : ").split(',')
list = [0 for i in range(len(var))]

for j in range(len(var)):
    list[j] = int(var[j],2)

a=0
for k in range(len(list)):
    if(list[k]%5==0):
        if(a==0): print(var[k],end='')
        else: print(', ',var[k],end='')
        a+=1