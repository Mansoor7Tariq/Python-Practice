from sumOfEvenAndOddNumbers import SumOfEven, SumOfOdd
from factorialOfN import FactorialOfN, OptimizedFactorial
from inputArray import inputArray
from palindrome import Palindrome, OptimizedPalindrom
from primeNumberCheck import isPrime
from FibonacciSequence import FibonacciSequence


def menu():
    print("Choose an option:")
    print("1. Sum even numbers")
    print("2. Sum odd numbers")
    print("3. Factorial of a number")
    print("4. check string is palindrom or not")
    print("5. check number is prime or not")
    print("6. check Fibonacci Sequence")

    choice = input("Enter your choice: ")
    # print("Array You Entered :", arr1)

    if choice == '1':
        arr1 = []
        arr1 = inputArray(arr1)
        print("Sum of even numbers:", SumOfEven(arr1))
    elif choice == '2':
        arr1 = []
        arr1 = inputArray(arr1)
        print("Sum of odd numbers:", SumOfOdd(arr1))
    elif choice == '3':
        num = int(input("Enter a number: "))
        # print("Factorial is:", FactorialOfN(num))
        print("Factorial is:", OptimizedFactorial(num))
    elif choice == '4':
        str = input("Enter a string: ")
        # print("The string is:", Palindrome(str))
        print("The string is:", OptimizedPalindrom(str))
    elif choice == '5':
        num = int(input("Enter a number: "))
        print("The number is:", isPrime(num))
    elif choice == '6':
        num = int(input("Enter a number: "))
        print("The Fibonacci Sequence is:", FibonacciSequence(num))
    else:
        print("Invalid choice")
