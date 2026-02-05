# ============================================
# EXCEPTION HANDLING – ALL IN ONE PYTHON FILE
# ============================================

# 1. Python script to CREATE an ArithmeticError
print("\n1. Creating ArithmeticError")
try:
    x = 10 / 0   # Division by zero
except Exception as e:
    print("ArithmeticError created:", e)


# 2. Python script to CREATE a ValueError
print("\n2. Creating ValueError")
try:
    num = int("abc")  # Invalid conversion
except Exception as e:
    print("ValueError created:", e)


# 3. Python script to HANDLE ArithmeticError
print("\n3. Handling ArithmeticError")
try:
    a = 20 / 0
except ArithmeticError:
    print("ArithmeticError handled successfully")


# 4. Python script to HANDLE ValueError
print("\n4. Handling ValueError")
try:
    value = int("xyz")
except ValueError:
    print("ValueError handled successfully")


# 5. Python script to HANDLE MULTIPLE exceptions in ONE try
print("\n5. Handling Multiple Exceptions")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 / num2)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# 6. Calculator with 4 basic operations and MAX exception handling
print("\n6. Calculator with Exception Handling")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        raise ValueError("Invalid operation selected")

except ValueError as ve:
    print("ValueError:", ve)
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print("Unexpected Error:", e)


# 7. Adding FINALLY block to the calculator
print("\n7. Calculator with FINALLY block")

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Division:", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution completed (finally block executed)")


# 8. Try-Except-Else block for DIVISION
print("\n8. Try-Except-Else Example")

try:
    m = int(input("Enter numerator: "))
    n = int(input("Enter denominator: "))
    result = m / n
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Enter valid integers")
else:
    print("Division Result:", result)


# 9. Python script to RAISE a ValueError
print("\n9. Raising a ValueError manually")

age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
else:
    print("Valid age:", age)


# 10. Nested Try-Except Block
print("\n10. Nested Try-Except Example")

try:
    num = int(input("Enter a number: "))
    try:
        result = 10 / num
        print("Result:", result)
    except ZeroDivisionError:
        print("Inner Try: Division by zero")
except ValueError:
    print("Outer Try: Invalid number input")


# ============================================
# END OF FILE
# ============================================
