min_price = 101
max_price = -1
total_in_range = 0
count_in_range = 0
while True:
    price = float(input())
    if price == -1:
        break
    if price < min_price:
        min_price = price
    if price > max_price:
        max_price = price
    if price >= 5 and price <= 30:
        total_in_range = total_in_range + price
        count_in_range = count_in_range + 1

if count_in_range > 0:
    avg_in_range = int(total_in_range / count_in_range)
else:
    avg_in_range = 0

print(int(max_price), int(min_price), avg_in_range)