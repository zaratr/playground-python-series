# Functions in Python


def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")


def calculate(a, b):
    """Return both the sum and product as a tuple."""
    return a + b, a * b


def welcome(name="Guest"):
    print(f"Welcome {name}")


def square(x):
    return x * x


def _run_examples():
    # Basic greeting examples
    greet("Alice", "Hi")
    greet("Python learner")

    # Demonstrate multiple return values
    a_example, b_example = 2, 3
    sum_, mul_ = calculate(a_example, b_example)
    print("=" * 40)
    print("Example 1: Unpacking multiple return values")
    print(f"Input: a = {a_example}, b = {b_example}")
    print(f"Sum (a + b): {sum_}")
    print(f"Product (a * b): {mul_}")
    print()

    # Using the raw tuple
    result_tuple = calculate(4, 5)
    print("Example 2: Using the returned tuple directly")
    print(f"Result as tuple: {result_tuple}")
    print(f"First value (sum): {result_tuple[0]}")
    print(f"Second value (product): {result_tuple[1]}")
    print()

    # More examples
    print("=" * 40)
    print("More examples")
    print("=" * 40)
    for a_val, b_val in [(10, 5), (7, 8), (2.5, 4), (-3, 5)]:
        s, p = calculate(a_val, b_val)
        print(f"calculate({a_val}, {b_val}): sum={s}, product={p}")
    print()

    # Square helper
    print(f"square(5) = {square(5)}")

    # Welcome demo
    welcome()
    welcome("Nishith")


if __name__ == "__main__":
    _run_examples()
