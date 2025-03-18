# Simple calculator for iTokyo day 7 (DIY Friday)
print("Python:Hey there 👋, what's your name")
name = input("User: ")
print(f"Python: Welcome to {name}'s calculator, what operation do you want to do")
operation = input("User: ")
print("Python: Enter Number 1")
num1 = input("User: ")
print("Python: Enter Number 2")
num2 = input("User: ")
# Convert inputs to numbers
number1 = float(num1)
number2 = float(num2)
# Perform the calculation based on operation
if operation.upper() == "ADD":
    #addition here
    result=number1+number2
elif operation.upper() == "SUBTRACT":
    #subtraction here
    result=number1-number2
elif operation.upper() == "MULTIPLY":
    #multiplication here
    result=number1*number2
elif operation.upper() == "DIVIDE":
    #division here
    result=number1/number2
else:
    result = "Unknown operation"

# Display the result
print(f"Python: The answer is {result}")
