try:
    fh = open("invalidpath/test.txt","w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error:can't find file to read data")
else:
    print("I will execute when no exception occurs")
finally:
    print("I am always executing")