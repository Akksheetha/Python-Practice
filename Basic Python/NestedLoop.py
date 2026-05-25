L = int(input("Enter lower limit : "))
U = int(input("Enter upper limit : "))
print("The prime numbers between",L,"and",U,"are:")
for num in range(L,U+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)