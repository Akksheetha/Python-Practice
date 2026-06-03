import re
text = "Alan Turing was a pioneer of theoritical computer science and artificial intelligence. He was born on 23 june 1912 in Maida Vale, London"
res = re.search('Turing',text)
print("Result = {} and start,end position = {}".format(res,res.span()))