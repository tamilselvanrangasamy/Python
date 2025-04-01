def max_of_three(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        print("num1 is maximum")
    elif(num2>=num3 and num2>=num1):
        print("num2 is maximum")
    else:
        print("num3 is maximum")
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
max_of_three(num1,num2,num3)
