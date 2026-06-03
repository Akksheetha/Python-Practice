import re
text = "Alan Turing was a pioneer of theoritical computer science and artificial intelligence. He was born on 23 june 1912 in Maida Vale, London"
res = re.search("computer",text)
print("Match object = {}".format(res))
print("Group method output = ",res.group())
print("Start method output = ",res.start())
print("end method output = ",res.end())
print("Span method output = ",res.span())
print("re attribute output = ",res.re)
print("string attribute output = ",res.string)
text = r'search \\ in the string'
res = re.search(r"\\",text)
print("With r as prefix = ",res)
