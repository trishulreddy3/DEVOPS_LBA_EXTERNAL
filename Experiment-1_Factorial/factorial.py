"""
Experiment 1.a: Factorial Calculation Program in Python
Calculates the factorial of a given non-negative integer.
Supports both interactive input and command-line argument.
"""

import sys

def factorial_iterative(n: int) -> int:
    """Calculate factorial iteratively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """Calculate factorial recursively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

def main():
    print("=" * 45)
    print("        DevOps Lab - Factorial Program        ")
    print("=" * 45)

    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
        except ValueError:
            print(f"[Error] Invalid argument '{sys.argv[1]}'. Please pass an integer.")
            sys.exit(1)
    else:
        try:
            user_input = input("Enter a non-negative integer: ")
            num = int(user_input)
        except ValueError:
            print("[Error] Invalid input. Please enter a valid integer.")
            sys.exit(1)

    try:
        fact = factorial_iterative(num)
        print(f"\n[Result] Factorial of {num} ({num}!) = {fact}")
        print("=" * 45)
    except ValueError as e:
        print(f"[Error] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
