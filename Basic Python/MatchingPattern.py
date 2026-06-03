import re
pattern = r'\b\w+ing\b'
text = "Walking and talking are important activities"
match_result = re.search(pattern,text)
if match_result:
    print("Match found :",match_result.group())
else:
    print("No match found")

