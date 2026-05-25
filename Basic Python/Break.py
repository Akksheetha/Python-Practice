N = int(input("Enter the value of N : "))
i = 1
sum = 0
while i<=N:
    num = int(input("Enter the user input : "))
    if num == -1:
        break
    else:
        sum = sum+num

    i=i+1
print("The sum of user input is: ",sum)