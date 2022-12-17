"""
Recursion is a programming technique that involves defining a function that calls itself.
It can be used to solve problems that can be broken down into smaller, repetitive subproblems.

A simple example of a recursive function is Python that calculates the factorial of a number:

"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) # Output: 120

"""
In this example, the `factorial` function calculates the factorial of a number `n` by calling
itself with `n-1` until it reaches the base case of `n=1`, at which point it returns 1.

Recursion can be powerful tool for solving problems, but it is important to ensure that the
base case is properly defines and that the recursive calls eventually terminate, or the 
function will continue to call itself indefinitely and result in an infinite loop.

It is also important to consider the performance of recursive functions, as they can be slower
and use more memory than iterative solutions due to the overhead of function calls. In some
cases, it may be more efficient to use an iterative solution instead of a recursive one.
"""