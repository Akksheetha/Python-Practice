import re
text = "Hi Akksheetha"
res = re.search("^H.*a$",text)
if(res):
    print("We have a match")
else:
    print("We don't have a match")
print(type(res))