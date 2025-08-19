# Fibonacci sequence generator in Python

def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    :param n: number of terms
    """
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
