import re
text = "Alan aTuringb was a pioneer of theoritical computer science and artificial intelligence. He was born on 23 june 1912 in Maida Vale, London"
res = re.findall('Turing',text)
print("Result = {}".format(res))
