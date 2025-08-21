'''3. Write a program to print all even numbers from 1 to N, where you have to take N as input 
from the user. 
Input:- N = 10 '''
N = int(input("Enter a number N: "))
for i in range(2, N + 1, 2):

    print(i, end=' ')   
