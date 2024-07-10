#The algorithmic steps for implementing recursio in a function are as follows:

#step1 - Define a base case: Identify the simplest case for which the soultion is known or trivial
# This is the stopping condition for the recursion.
# as it prevents the function from infinitely calling itself

#step2 -  Define a recursive case: Define the problem in terms of similar subproblems
# break the problem down into similar versions of itself, and call the function recursively to solve each subproblem

#step3 - Ensure the recursion terminiates: Make sure that the recursive function eventually reaches the base case,
# and does not enter an infinite loop


# step4- combine the solutions: Combine the soultions of the subproblems to solve the original problem.

"""
#in the recursive program, the solution to the base case is provided
#and the solution to the bigger problem is expressed in terms of smaller problems

int fact(int n)
{
    if (n < = 1) // base case
        return 1;
    else
        return n*fact(n-1);
}
#in the above example, the base case for n < = 1 is defined and the larger value of a number can be solved
#by converting to a smaller one till the base case is reached.
"""

#Writing a program using the concepts of recursion to find the factorial of the non negative integer number

def factorial(n):
    #base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    #recursive case: factorial of n is n * factorial of (n-1)
    else:
        return n * factorial(n-1)

#Input from user
num = int(input("enter a non-negative integer to calculate its factorial: "))

#Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
