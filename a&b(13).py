'''13. Write a program to input two numbers(A & B) from the user and print the maximum 
element among A & B. '''
a = int(input("Enter first number (A): "))
b = int(input("Enter second number (B): ")) 
if a > b:
    print("Maximum element is:", a)
else:
    print("Maximum element is:", b)