x = int(input())
y = int(input())
sum_x = 0
for i in range(1, x):
    if x % i == 0:
        sum_x = sum_x + i
sum_y = 0
for i in range(1, y):
    if y % i == 0:
        sum_y = sum_y + i
if sum_x == y and sum_y == x:
    print("Amicable Pair")
else:
    print("Not an Amicable pair")