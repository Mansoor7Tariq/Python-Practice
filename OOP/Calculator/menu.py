from Addition import Addition
from Subtraction import Subtraction
from Division import Division
from Multiply import Multiplication


def menu():
    choice = 0
    while choice != '-1':
        print("Choose an option:")
        print("1. Sum")
        print("2. Subtract")
        print("3. Division")
        print("4. Multiplay")
        print("-1. For Exit")

        choice = input("Enter your choice: ")

        if choice == '-1':
            print("Calculator in Python")
        else:
            number1 = int(input("Enter Number One : "))
            number2 = int(input("Enter Number Two : "))
            if choice == '1':
                Add = Addition(number1, number2)
                Add.Calculate()
                print("Sum :", Add.GetResult())
            elif choice == '2':
                Subtract = Subtraction(number1, number2)
                Subtract.Calculate()
                print("Subtraction :", Subtract.GetResult())
            elif choice == '3':
                Divide = Division(number1, number2)
                Divide.Calculate()
                print("Division :", Divide.GetResult())
            elif choice == '4':
                Multiply = Multiplication(number1, number2)
                Multiply.Calculate()
                print("Multiplication :", Multiply.GetResult())
            else:
                print("Invalid choice")
