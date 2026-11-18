"""
Experiment 4.a: Arithmetic Operations in Python
Supports Addition, Subtraction, Multiplication, and Division.
Includes CLI args, interactive menu, and modular functions.
"""

import sys

def add(a: float, b: float) -> float:
    """Return sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return difference of a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return quotient of a divided by b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b

def compute(operation: str, a: float, b: float) -> float:
    """Execute given operation name."""
    op = operation.strip().lower()
    if op in ('add', '+', 'addition'):
        return add(a, b)
    elif op in ('sub', 'subtract', '-', 'subtraction'):
        return subtract(a, b)
    elif op in ('mul', 'multiply', '*', 'multiplication'):
        return multiply(a, b)
    elif op in ('div', 'divide', '/', 'division'):
        return divide(a, b)
    else:
        raise ValueError(f"Unknown operation: '{operation}'. Choose add, sub, mul, or div.")

def main():
    print("=" * 48)
    print("      DevOps Lab - Arithmetic Operations        ")
    print("=" * 48)

    # CLI Argument mode: python arithmetic.py <op> <a> <b>
    if len(sys.argv) == 4:
        op = sys.argv[1]
        try:
            a = float(sys.argv[2])
            b = float(sys.argv[3])
            res = compute(op, a, b)
            # Format integer outputs cleanly
            if res.is_integer():
                res = int(res)
            print(f"[Result] {op.upper()} ({a}, {b}) = {res}")
            print("=" * 48)
            return
        except ValueError as e:
            print(f"[Error] {e}")
            sys.exit(1)
        except ZeroDivisionError as e:
            print(f"[Math Error] {e}")
            sys.exit(1)

    # Interactive CLI menu
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("-" * 48)

    choice = input("Enter choice (1-5): ").strip()
    if choice == '5':
        print("Exiting...")
        return

    op_map = {'1': 'add', '2': 'sub', '3': 'mul', '4': 'div'}
    if choice not in op_map:
        print("[Error] Invalid choice.")
        sys.exit(1)

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        res = compute(op_map[choice], num1, num2)
        if res.is_integer():
            res = int(res)
        print(f"\n[Result] Result = {res}")
        print("=" * 48)
    except ValueError as e:
        print(f"[Error] Invalid numeric input: {e}")
        sys.exit(1)
    except ZeroDivisionError as e:
        print(f"[Math Error] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
