try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    c = a/b
except(ZeroDivisionError):
    print("Can't divide by zero")
else:
    print("No exception occured")
print("Successfully executed")