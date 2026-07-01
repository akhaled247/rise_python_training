import math

class BasicOperators:

    def __init__(self):
        pass

    def calculate(self, operator, a=0.000, b=0.000):
        match(operator):
            case Calculator.Operators.SUM:
                return a+b
            case Calculator.Operators.DIFFERENCE:
                return a-b
            case Calculator.Operators.PRODUCT:
                return a*b
            case Calculator.Operators.QUOTIENT:
                return a/b 

class Calculator(BasicOperators):
    class Operators:
        SUM = "sum"
        DIFFERENCE = "difference"
        PRODUCT = "product"
        QUOTIENT = "quotient"

        def find_operator_from_str(self, input):
            match(input):
                case "sum":
                    return self.SUM
                case "difference":
                    return self.DIFFERENCE
                case "product":
                    return self.PRODUCT
                

def main() -> None:
    calculator = Calculator()
    operators = Calculator.Operators
    while True: 
        print(calculator.calculate(
                operators.find_operator_from_str(operators, input=input("What operation:")),
                float (input("What is your first number: ")),
                float (input("What is your second number: "))))

if __name__ == "__main__":
    main()