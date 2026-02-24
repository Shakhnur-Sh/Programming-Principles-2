# generators.py
# Python iterators and generators

# 1) squares up to N
def squares_up_to_n(n: int):
    """Generate squares of numbers from 1 to n."""
    for i in range(1, n + 1):
        yield i * i

# 2) even numbers 0..n in comma-separated form
def even_numbers_comma(n: int):
    """Generate even numbers from 0 to n."""
    for x in range(0, n + 1):
        if x % 2 == 0:
            yield x

# 3) numbers divisible by 3 and 4 from 0..n
def divisible_by_3_and_4(n: int):
    """Generate numbers divisible by both 3 and 4 (i.e., by 12) from 0 to n."""
    for x in range(0, n + 1):
        if x % 3 == 0 and x % 4 == 0:
            yield x

# 4) squares from a to b
def squares(a: int, b: int):
    """Yield squares of all numbers from a to b (inclusive)."""
    step = 1 if a <= b else -1
    for x in range(a, b + step, step):
        yield x * x

# 5) countdown from n to 0
def countdown(n: int):
    """Generate numbers from n down to 0."""
    for x in range(n, -1, -1):
        yield x

# Main function to demonstrate the generators
def main():
    # 1) squares up to N
    n = int(input("Enter N for squares (1..N): "))
    for val in squares_up_to_n(n):
        print(val)

    # 2) even numbers 0..n in comma-separated form
    n2 = int(input("\nEnter n for even numbers (0..n): "))
    print(",".join(str(x) for x in even_numbers_comma(n2)))

    # 3) numbers divisible by 3 and 4 from 0..n
    n3 = int(input("\nEnter n for numbers divisible by 3 and 4 (0..n): "))
    print(" ".join(str(x) for x in divisible_by_3_and_4(n3)))

    # 4) squares from a to b
    a = int(input("\nEnter a for squares(a..b): "))
    b = int(input("Enter b for squares(a..b): "))
    for val in squares(a, b):
        print(val)

    # 5) countdown from n to 0
    n4 = int(input("\nEnter n for countdown (n..0): "))
    for val in countdown(n4):
        print(val, end=" ")
    print()

# Run the main function
if __name__ == "__main__":
    main()