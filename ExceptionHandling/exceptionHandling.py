# try:
#     even_numbers = [2, 4, 6, 8]

#     numerator = 10
#     denominator = 0
#     result = numerator/denominator
#     print('Result is:', result)
#     print(even_numbers[10])


# except ZeroDivisionError:
#     print("Denominator cannot be 0.")

# except IndexError:
#     print("Index Out of Bound.")

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input! Please enter integers.")
else:
    print(f"The result of division is: {result}")
finally:
    print("This block will always be executed, regardless of exceptions.")
