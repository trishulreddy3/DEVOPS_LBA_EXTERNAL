"""
Experiment 2.a: Prime Number Checker in Python
Checks whether a given number is prime.
Optimized O(sqrt(n)) algorithm.
"""

import sys
import math

def is_prime(n: int) -> bool:
    """Check if an integer n is prime."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def get_prime_details(n: int) -> dict:
    """Return dictionary with prime check and explanation."""
    prime_status = is_prime(n)
    if n <= 1:
        reason = f"{n} is not prime because prime numbers must be greater than 1."
    elif prime_status:
        reason = f"{n} is a prime number (only divisible by 1 and itself)."
    else:
        # Find the smallest factor
        factor = 2 if n % 2 == 0 else 3
        if factor not in (2, 3):
            for i in range(5, int(math.isqrt(n)) + 1, 2):
                if n % i == 0:
                    factor = i
                    break
        reason = f"{n} is composite (divisible by {factor})."
    return {"number": n, "is_prime": prime_status, "reason": reason}

def main():
    print("=" * 45)
    print("        DevOps Lab - Prime Number Checker     ")
    print("=" * 45)

    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
        except ValueError:
            print(f"[Error] Invalid argument '{sys.argv[1]}'. Must be an integer.")
            sys.exit(1)
    else:
        try:
            user_input = input("Enter an integer to check: ")
            num = int(user_input)
        except ValueError:
            print("[Error] Invalid input. Must be an integer.")
            sys.exit(1)

    details = get_prime_details(num)
    status_str = "PRIME" if details["is_prime"] else "NOT PRIME"
    print(f"\n[Result] Number {num} is {status_str}")
    print(f"[Details] {details['reason']}")
    print("=" * 45)

if __name__ == "__main__":
    main()
