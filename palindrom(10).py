'''10. You are given an integer A as input, and you need to determine whether it is a palindrome 
or not. A palindrome integer is one whose digits, when reversed, result in the same number. 
For example, 121 is a palindrome because its reverse is also 121, but 123 is not a palindrome 
because its reverse is 321.Note: The given integer will not have any leading zeros. '''
A = int(input("Enter a positive integer A: "))
original_number = A
reversed_number = 0
while A > 0:
    digit = A % 10
    reversed_number = reversed_number * 10 + digit
    A //= 10
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")