'''2. Write a program to print all Natural numbers from N to 1, where you have to take N as input 
from the user. '''
N = int(input("Enter a positive integer N: "))
for i in range(N, 0, -1):
    print(i, end=' ')
