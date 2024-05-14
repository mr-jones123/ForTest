def addNumbers(num1,num2):
    return num1 + num2

def substractNumbers(num1,num2):
    return num1 - num2

def divideNumbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed"
    return num1 / num2
number1 = int(input(">"))

number2 = int(input(">"))

print(substractNumbers(number1, number2))

print(addNumbers(number1, number2))


