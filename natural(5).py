'''5. Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as 
input from user '''
N = int(input("Enter a positive integer N: "))
sum_of_natural_numbers = sum(range(1, N + 1))
print(f"The sum of all natural numbers from 1 to {N} is: {sum_of_natural_numbers}")

