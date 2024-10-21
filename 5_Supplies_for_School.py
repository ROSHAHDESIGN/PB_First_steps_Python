# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)
PENS = 5.8
MARKERS = 7.2
CLEANER = 1.2

num_pens = int(input())
num_markers = int(input())
liter_cleaner = int(input())
discount = int(input())

price_pens = num_pens * PENS
price_markers = num_markers * MARKERS
price_cleaner = liter_cleaner * CLEANER
discount_percentage = discount / 100
costs = price_pens + price_markers + price_cleaner
costs_with_discount = costs - (costs*discount_percentage)

print(costs_with_discount)

