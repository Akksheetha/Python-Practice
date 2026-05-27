my_tuple = ()
my_tuple = (10,20,30,40,50)
print(type(my_tuple))
my_tuple = (10,3.14,'ram',50)
print(type(my_tuple))
my_tuple = 10,3.14,'ram',50
print(type(my_tuple))
my_tuple = 10,3.14,'ram',[1,2,3]
print(type(my_tuple))
#print(type(my_tuple[5[1]]))
t = (10,20,30,40,50)
t = (100,)+t[1:]
print(t)
addr = "monty@python.org"
uname, domain = addr.split('@')
print(uname)
print(domain)
