MyFamily = {"child1":{"name":"Ram","year":2004},
            "child2":{"name":"Sita","year":2007}}
print(MyFamily["child2"]["name"])
thisdict = {"brand":"ford","model":"Mustang","year":1964}
print(thisdict)
del thisdict['model']
print(thisdict)
del thisdict
dict1 = {"brand":"Ford","model":"Mustang","year":1964}
for x in dict1:
    print(x,dict1[x])

d = {1:"one",2:"three"}
d1 = {2:"two"}
d.update(d1)
print(d)