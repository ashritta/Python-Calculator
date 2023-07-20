import calculator

selection = int(input("Select your calculator operation: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nYour Choice: "))

num1 = int(input("Provide your 1st value: "))
num2 = int(input("Provide your 2nd value: "))
ans = 0

if selection == 1:
    ans = calculator.add(num1, num2)
elif selection == 2:
    ans = calculator.subtract(num1, num2)
elif selection == 3:
    ans = calculator.multiply(num1, num2)
elif selection == 4:
    if num2 == 0:
        print("Cannot divide by 0!")
    else:
        ans = round(calculator.divide(num1, num2), 2)
else:
    print("Your selection was not a valid choice")

print(f"Your result is {ans}")