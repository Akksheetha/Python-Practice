class Error(Exception):
    """BaseClass for other exceptions"""
    pass
class valueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

number = 10
while True:
    try:
        i_num = int(input("Enter a number : "))
        if i_num<number:
            raise valueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except valueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, Try again")
print("Congratulations! You guessed it correcly")