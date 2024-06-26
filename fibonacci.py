def fibonacci(n):
    """
    Generate the first n Fibonacci numbers.
    
    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list containing the first n Fibonacci numbers.
    """
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate the next Fibonacci numbers until we have n numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence[:n]

# Example usage:
num = 10  # Number of Fibonacci numbers to generate
fibonacci_numbers = fibonacci(num)
print(fibonacci_numbers)
