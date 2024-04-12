#!/usr/bin/env python3
#!/usr/bin/env python3

def print_fibonacci(length):
    '''Prints Fibonacci sequence up to a given length.'''
    fib_sequence = []
    if length >= 1:
        fib_sequence.append(0)
    if length >= 2:
        fib_sequence.append(1)
    for i in range(2, length):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print(fib_sequence)

if __name__ == "__main__":
    print_fibonacci(10)
