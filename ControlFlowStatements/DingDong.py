start = int(input("Enter the Starting number : "))
end = int(input("Enter the ending number : "))
for i in range(start, end + 1):
    if i % 10 == 0:
        print("dong", end=" ")
    elif i % 5 == 0:
        print("ding", end=" ")
    else:
        print(i, end=" ")
print()