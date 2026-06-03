def file_to_list(file_path):
    f=open(file_path,"r")
    l=f.read().splitlines()
    f.close()
    return l

file_path=input("Enter file name: ")
print(file_to_list(file_path))
