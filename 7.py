"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
"""
import numpy as np
X,Y = input("Enter 2 digits : ").split(',')
data = np.zeors([int(X),int(Y)])

for i in range(X):
    for j in range(Y):
        data[i,j] = i*j

#numpy를 설치해야된다는데 인터넷에서 하라는대로 해도 안돼요ㅠㅠㅠ