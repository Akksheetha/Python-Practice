def add_mul(num1,num2,num3=4):
    out = (num1+num2)*num3
    return out
val1 = int(input("Enter first integer : "))
val2 = int(input("Enter secod integer : "))
result = add_mul(val1,val2)
print(result)