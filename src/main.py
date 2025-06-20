def main():
    from calculator import Calculator
    from utils import validate_number, format_result

    calculator = Calculator()

    while True:
        print("Welcome to the Calculator!")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1_input = input("Enter first number: ")
            num2_input = input("Enter second number: ")

            # 使用 validate_number 验证输入
            if not validate_number(num1_input) or not validate_number(num2_input):
                print("Invalid input! Please enter valid numbers.")
                continue

            num1 = float(num1_input)
            num2 = float(num2_input)

            if choice == '1':
                result = calculator.add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = calculator.subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = calculator.multiply(num1, num2)
                operation = "Multiplication"
            elif choice == '4':
                result = calculator.divide(num1, num2)
                operation = "Division"

            # 使用 format_result 格式化输出
            print(format_result(result))
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()