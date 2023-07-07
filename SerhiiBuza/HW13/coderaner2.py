"""
Write fibonacci_numbers function which returns a generator that yields the Fibonacci sequence.
"""

def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
    
    
fib = fibonacci_numbers()

for i in range(10):
    print(next(fib))