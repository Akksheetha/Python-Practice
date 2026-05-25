num_str = input()
num_len = len(num_str)
total = 0
for char in num_str:
    digit = int(char)
    total = total + (digit ** num_len)
if total == int(num_str):
    print("true")
else:
    print("false")