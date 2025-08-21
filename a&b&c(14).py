'''14. Write a program to input three numbers(A, B & C) from the user and print the 
minimum element among A, B & C. '''
a = int(input("Enter first number  "))
b = int(input("Enter second number  ")) 
c = int(input("Enter third number  "))
if a < b and a < c:
    print("Minimum element is:", a)
elif b < a and b < c:
    print("Minimum element is:", b)
elif c < a and c < b:
    print("Minimum element is:", c)
else:
    print("element is equal:")

