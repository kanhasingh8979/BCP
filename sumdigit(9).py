'''
9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the 
given number N. '''
N = int(input("Enter a positive integer N: "))
sum_of_digits = sum(int(digit) for digit in str(N))
print(f"The sum of the digits of {N} is: {sum_of_digits}")
