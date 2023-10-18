import math

def calculate(num1, num2, operator):
  """Calculates the result of two numbers based on the given operator.

  Args:
    num1: The first number.
    num2: The second number.
    operator: The operator to use.

  Returns:
    The result of the calculation.
  """

  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  else:
    raise ValueError("Invalid operator.")


if __name__ == "__main__":
  # Prompt the user for the two numbers and the operator.
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter the operator (+, -, *, or /): ")

  # Calculate the result.
  result = calculate(num1, num2, operator)

  # Print the result.
  print(result)