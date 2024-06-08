
print("Select an operator to perform:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
operation=input()
if operation=='1':
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print("The Sum is: ",num1+num2)
elif operation=='2':
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print("The Difference is: ",num1-num2)
elif operation=='3':
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print("The Product is: ",num1*num2)
elif operation=='4':
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print("The Result is: ",num1/num2)
else:
    print("Invalid Option !!")
