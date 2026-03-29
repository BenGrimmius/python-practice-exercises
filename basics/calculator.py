"""
Calculator Challenge Rules:
---------------------------
- Build a simple command-line calculator that:
  1. Asks the user to enter two numbers.
  2. Asks the user to choose an operation: +, -, *, or /.
  3. Performs the chosen operation and prints the result.
  4. Handles invalid input (e.g., non-numeric values, unsupported operations).
  5. Handles division by zero with an error message instead of crashing.
"""

def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number.")


def get_operation() -> str:
    valid_operations = {"+", "-", "*", "/", "q"}

    while True:
        print("\nChoose an operation:")
        print("+  Add")
        print("-  Subtract")
        print("*  Multiply")
        print("/  Divide")
        print("q  Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice in valid_operations:
            return choice

        print("Invalid choice. Please enter +, -, *, /, or q.")


def main() -> None:
    print("Welcome to the Calculator")

    while True:
        operation = get_operation()

        if operation == "q":
            print("Goodbye.")
            break

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)

            print(f"Result: {result}")

        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()