def storingNumbers(num):
    my_dict = {1:"One",2:"Two",3:"Three",4:"Four",5:"five",6:"six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
    return my_dict[int(num)]

num = str(input("Enter a number : "))
for i in num:
    ans = storingNumbers(i)
    print(ans,end = " ")