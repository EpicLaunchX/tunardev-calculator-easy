from domain.models import operands_factory
from service.calculator import Calculator


def main():
    calculator = Calculator()

    first_operand = int(input("Enter the first operand: "))
    second_operand = int(input("Enter the second operand: "))
    action = input("Enter the action (add, subtract, multiply, divide): ").strip().lower()

    operands = operands_factory(first_operand, second_operand)

    if action == "add":
        result = calculator.add(operands)
    elif action == "subtract":
        result = calculator.subtract(operands)
    elif action == "multiply":
        result = calculator.multiply(operands)
    elif action == "divide":
        try:
            result = calculator.divide(operands)
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid action.")
        return

    print(f"Result: {result}")
