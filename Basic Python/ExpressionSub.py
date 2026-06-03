import re
text = "Alan Turing was a pioneer of theoretical computer science and artificial intelligence. He was born on 23 june 1912 in Maida Vale, London"
res = re.sub('theoretical','practical',text)
print("Result = {}".format(res))