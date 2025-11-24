def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
try:
    num = int(input("Enter a number to find its factorial: "))
    print("Factorial:", factorial(num))

except ValueError as ve:
    print("Error:", ve)

except Exception:
    print("Invalid input. Please enter an integer value.")