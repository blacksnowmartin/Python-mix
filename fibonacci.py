def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the nth term.

    Args:
        n: The number of terms to generate.

    Returns:
        A list containing the Fibonacci sequence up to the nth term.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        list_fib = [0, 1]
        while len(list_fib) < n:
            next_fib = list_fib[-1] + list_fib[-2]
            list_fib.append(next_fib)
        return list_fib

def test_fibonacci_sequence():
    """
    Tests the fibonacci_sequence function with several test cases.
    """
    print("Testing fibonacci_sequence function:")
    test_cases = [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ]

    for n, expected_output in test_cases:
        actual_output = fibonacci_sequence(n)
        if actual_output == expected_output:
            print(f"Test case for n = {n} passed!")
        else:
            print(f"Test case for n = {n} failed. Expected: {expected_output}, Actual: {actual_output}")

# Run the tests
test_fibonacci_sequence()
