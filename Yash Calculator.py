def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num1 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
operation = input("Enter the operation (+ for addition, - for subtraction, * for multiplication, / for division): ")        
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = calculate(num1, num2, operation)
print("result is :")
print(f"{num1} {operation} {num2} ={result}")