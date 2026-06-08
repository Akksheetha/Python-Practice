class StringProcessor:
    def ProcessString(self, s, operation=None):
        if operation == "upper":
            return s.upper()
        elif operation == "reverse":
            return s[::-1]
        else:
            return len(s)
sp = StringProcessor()
print(sp.ProcessString("hello", "upper"))
print(sp.ProcessString("hello", "reverse"))
print(sp.ProcessString("hello"))