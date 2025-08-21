'''6. You are given an integer A, you need to find and return the sum of all the even numbers 
between 1 and A. Even numbers are those numbers that are divisible by 2. '''
A = int(input("Enter a number A: "))
sum_of_even_numbers = sum(range(2, A + 1, 2))
print(f"The sum of all even numbers  is: {sum_of_even_numbers}")

