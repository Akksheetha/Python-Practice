from math import sin, cos, radians
deg = float(input().split()[0])
rad = radians(deg)
print(f"sin({int(deg)}) = {round(sin(rad), 1)}")
print(f"cos({int(deg)}) = {round(cos(rad), 1)}")