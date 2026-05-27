def menu():
    my_list = []
    while True:
        print("1.Add element")
        print("2.Insert element")
        print("3.Append element")
        print("4.Modify element")
        print("5.Remove an element")
        print("6.Delete or pop an element")
        print("7.Sort in Ascending order")
        print("8.Sort in Descending order")
        print("9.Display the list")
        print("10.Exit")

        num = int(input("Enter your choice : "))
        if num == 1:
            element = input("Enter element to add : ")
            my_list += [element]
            print("List :", my_list)
        elif num == 2:
            position = int(input("Enter position : "))
            element = input("Enter element : ")
            my_list.insert(position, element)
            print("List :", my_list)
        elif num == 3:
            element = input("Enter element to append : ")
            my_list.append(element)
            print("List :", my_list)
        elif num == 4:
            position = int(input("Enter position to modify : "))
            element = input("Enter new value : ")
            my_list[position] = element
            print("List :", my_list)
        elif num == 5:
            element = input("Enter element to remove : ")
            my_list.remove(element)
            print("List :", my_list)
        elif num == 6:
            position = int(input("Enter position to delete : "))
            my_list.pop(position)
            print("List :", my_list)
        elif num == 7:
            my_list.sort()
            print("Ascending order :", my_list)
        elif num == 8:
            my_list.sort(reverse=True)
            print("Descending order :", my_list)
        elif num == 9:
            print("Current List :", my_list)
        elif num == 10:
            print("Exiting program...")
            break
        else:
            print("Invalid choice")
menu()